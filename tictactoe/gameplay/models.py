from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

GAME_STATUS_CHOICES = (
    ('F', "first player to move"),
    ('S', "second player to move"),
    ('W', "first player wins"),
    ('L', "second player wins"),
    ('D', "draw")
)

class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player = user) | Q(second_player = user)
        )

    def active(self):
        return self.filter(
            Q(status = 'F') | Q(status = 'S')
        ).count()

# Create your models here.
@python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player",
        on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name="games_second_player",
        on_delete=models.CASCADE)

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=GAME_STATUS_CHOICES, default='F')
    move_count = models.IntegerField(default=0)

    objects = GamesQuerySet.as_manager()

    def __str__(self):
        return "{0} vs. {1}, turn {2}".format(self.first_player, self.second_player, self.move_count)

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    byFirstPlayer = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
