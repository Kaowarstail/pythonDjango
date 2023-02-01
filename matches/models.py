from django.db import models
from model_utils.models import TimeStampedModel


class Game(TimeStampedModel):
    """Model a notion of a Game.
    """
    home_team = models.ForeignKey("members.Team", on_delete=models.PROTECT, related_name='home_games')
    away_team = models.ForeignKey("members.Team", on_delete=models.PROTECT, related_name='away_games')
    date = models.DateField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} - {self.away_team}"


class Call(TimeStampedModel):
    
    class Status(models.TextChoices):
        AWAITING_REPLY = 'awaiting', "Awaiting reply"
        ACCEPTED = 'accepted', "Accepted"
        REFUSED = 'refused', "refused"

    game = models.ForeignKey(Game, related_name="calls", on_delete=models.CASCADE)
    member = models.ForeignKey("members.MemberTeam", related_name="calls", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AWAITING_REPLY)

    def __str__(self):
        return f"{self.game} {self.member}"