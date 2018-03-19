from django.shortcuts import render
from django.db.models import Q
from gameplay.models import Game

# Create your views here.
def home(request):
    games_first_player = Game.objects.filter(
        first_player = request.user,
        status = 'F'
    )

    games_second_player = Game.objects.filter(
        second_player = request.user,
        status = 'S'
    )

    all_my_games = list(games_first_player) + list(games_second_player)

    return render(request, "player/home.html",
        {
            'ngames' : Game.objects.count(),
            'nactivegames' : Game.objects.filter(Q(status='F') | Q(status='S')).count(),
            'allmygames' : all_my_games
        })
