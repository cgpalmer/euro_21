from django.shortcuts import render
from .models import Players, Teams

# Create your views here.
def index(request):
    players = Players.objects.all().order_by('-current_score')
    teams = Teams.objects.all()
    context = {
        'players': players,
        'teams': teams
    }
    return render(request, 'home/index.html', context)