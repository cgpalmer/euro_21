from django.shortcuts import render
from .models import Players, Teams

# Create your views here.
def index(request):
    players = Players.objects.all().order_by('-current_score')
    teams = Teams.objects.all()
    goals_for = Players.objects.all().order_by('-total_goals_for')
    goals_against = Players.objects.all().order_by('-total_goals_against')
    context = {
        'players': players,
        'teams': teams,
        'goals_for': goals_for,
        'goals_against': goals_against
    }
    return render(request, 'home/index.html', context)