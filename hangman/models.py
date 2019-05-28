from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """
    Stores the game data
    """
    # Database fields
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    chance_remaining = models.IntegerField()
    letters_guessed = models.CharField(
        max_length=25, blank=True, null=True)
    selected_word = models.CharField(max_length=25)
    space_filled = models.CharField(
        max_length=25, blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "Game: {}".format(self.id)
