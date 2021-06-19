from django.shortcuts import render
from .models import Players, Teams

# Create your views here.
def index(request):
    players = Players.objects.all().order_by('-current_score')
    teams = Teams.objects.all()
    goals_for = Players.objects.all().order_by('-total_goals_for')
    goals_against = Players.objects.all().order_by('-total_goals_against')
    own_goals = Players.objects.all().order_by('-own_goals')
    context = {
        'players': players,
        'teams': teams,
        'goals_for': goals_for,
        'goals_against': goals_against,
        'own_goals': own_goals,
    }
    return render(request, 'home/index.html', context)