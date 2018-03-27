from django.shortcuts import render
from gameplay.models import Game

# Create your views here.
def home(request):

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
        {
            'ngames' : Game.objects.count(),
            'nactivegames' : active_games,
            'allmygames' : my_games,
            'testparam' : request.GET.get('test', 'none')
        })
