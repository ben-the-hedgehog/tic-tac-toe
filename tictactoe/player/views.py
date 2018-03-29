from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game
from .models import Invitation
from .forms import InvitationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required
def home(request):

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    my_invites = request.user.invitations_received.all()

    return render(request, "player/home.html",
        {
            'ngames' : Game.objects.count(),
            'nactivegames' : active_games,
            'allmygames' : my_games,
            'allmyinvites' : my_invites,
            'testparam' : request.GET.get('test', 'none')
        })

@login_required
def new_invitation(request):
    if request.method == "GET":
        form = InvitationForm()
    elif request.method == "POST":
        invitation = Invitation(from_player=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_home")

    return render(request, "player/new_invitation_form.html", {'form' : form })

@login_required
def view_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not invitation.to_player == request.user:
        raise PermissionDenied
    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player = invitation.from_player,
                second_player = invitation.to_player
            )
        invitation.delete()
        return redirect("player_home")
    else:
        return render(request, "player/view_invitation.html", {'invitation' : invitation})
