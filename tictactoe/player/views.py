from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
