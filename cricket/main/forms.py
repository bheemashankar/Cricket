"""main forms module"""
from django import forms
from .models import Team, Matches


class MatchFixture(forms.Form):
    """Match for multiple choice class"""
    teams = forms.ModelMultipleChoiceField(queryset=Team.objects.all(),
                                           required=True,
                                           widget=forms.CheckboxSelectMultiple())


class MatchUpdate(forms.ModelForm):
    """Match update"""
    class Meta:
        """Meta class"""
        model = Matches
        fields = ('winner_team',)

    def __init__(self, *args, **kwargs):
        super(MatchUpdate, self).__init__(*args, **kwargs)
        self.fields['winner_team'] = forms.ChoiceField(choices=[])
