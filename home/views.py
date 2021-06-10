from django.shortcuts import render
from .models import Players

# Create your views here.
def index(request):
    players = Players.objects.all()
    context = {
        'players': players
    }
    return render(request, 'home/index.html', context)