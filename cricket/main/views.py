import copy
import random
from django.views.generic import ListView, DetailView, FormView
from main.models import Team, Player, Matches
from main.forms import MatchFixture, MatchUpdate
from django.urls import reverse_lazy
from .utils import rb_mixture
from django.views.generic import UpdateView
from cricket.settings import MATCH_CHOICE
from django.db.models import Q

# Create your views here.


class TeamListView(ListView):
    model = Team
    template_name = "team_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_list'] = self.model.objects.all()
        return context
    

class TeamDetailView(DetailView):
    model = Team
    template_name = "team_details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_details'] = Player.objects.filter(team__id=self.kwargs.get("pk"))
        return context
    
    
class MatchesListView(FormView):
    success_url = reverse_lazy('main:matches')
    form_class = MatchFixture
    template_name = "matches.html"

    def form_valid(self, form):
        team_ids = form.data.getlist('teams')
        random.shuffle(team_ids)
        for each in rb_mixture(team_ids, sets=len(team_ids) * 2 - 2):
            for one in each:
                l_team = Team.objects.get(pk=int(one[0]))
                r_team = Team.objects.get(pk=int(one[1]))
                Matches.objects.create(left_team=l_team, right_team=r_team)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches_list'] = Matches.objects.all()
        return context
    

class MatchUpdateView(UpdateView):
    model = Matches
    form_class = MatchUpdate
    template_name = 'match_edit_form.html'
    success_url = reverse_lazy("main:matches")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['match'] = self.object
        return context
    
    def get_form(self, form_class=None):
        choice = copy.copy(MATCH_CHOICE)
        form = super(MatchUpdateView, self).get_form(form_class)
        if len(choice) > 3:
            choice = copy.copy(MATCH_CHOICE)
        choice.insert(0, (self.object.left_team.id, self.object.left_team.name))
        choice.insert(1, (self.object.right_team.id, self.object.right_team.name))
        form.fields['winner_team'].choices = choice
        return form

    def form_valid(self, form):
        form.save()
        return UpdateView.form_valid(self, form)
    
    
class PointsListView(ListView):
    model = Team
    template_name = "points_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = self.model.objects.all()
        context['points_list'] = []
        for each in teams:
            won = Matches.objects.filter(winner_team=each.id)
            draw = Matches.objects.filter(winner_team=-2).filter(Q(left_team_id=each.id) | Q(right_team_id=each.id))
            context['points_list'].append((each, (len(won)*2)+(len(draw)*1)))        
        return context

