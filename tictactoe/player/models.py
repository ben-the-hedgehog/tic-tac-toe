from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Invitation(models.Model):
    from_player = models.ForeignKey(
        User,
        related_name="invitations_sent",
        on_delete=models.CASCADE
    )
    to_player = models.ForeignKey(
        User,
        related_name="invitations_received",
        verbose_name="User to invite",
        help_text="Select the player you want to play with",
        on_delete=models.CASCADE
    )
    message = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Optional message",
        help_text="It's always nice to include a message!"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
