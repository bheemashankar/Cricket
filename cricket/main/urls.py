from django.urls import path
from main.views import TeamListView, TeamDetailView, MatchesListView, MatchUpdateView,\
    PointsListView

app_name = "main"

urlpatterns = [
    path('',  TeamListView.as_view(), name="welcome"),
    path('teams/',  TeamListView.as_view(), name="teams"),
    path('teams/<int:pk>/details', TeamDetailView.as_view(), name="team_details" ),
    path('matches/', MatchesListView.as_view(), name="matches" ),
    path('match/<int:pk>/update', MatchUpdateView.as_view(), name="match_update" ),
    path('points', PointsListView.as_view(), name="points" )
]

