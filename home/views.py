from django.shortcuts import render
from .models import Players, Teams, Matches, Individual_teams
from .forms import MatchesForm
from django.contrib.auth.decorators import login_required

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

@login_required
def add_match(request, match_id):
    if request.method == 'POST':
        form = MatchesForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
          
            return render(request, 'home/index.html', context)
        else:
            return render(request, 'home/index.html', context)
    else:
        form = MatchesForm()
        template = 'home/add_match.html'
        context = {
                'form': form,
        }
        return render(request, template, context)