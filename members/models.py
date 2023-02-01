import uuid
from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    PLAYER = 'PLAYER', _('Player')
    COACH = 'COACH', _('Coach')


class Team(TimeStampedModel):
    name = models.CharField(max_length=100)
    club = models.ForeignKey("club.Club", related_name="teams", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.club} {self.name}"


class Member(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=250)
    team = models.ManyToManyField(Team, through="MemberTeam", related_name="members")

    def __str__(self):
        return self.full_name


class MemberTeam(TimeStampedModel):
    """A member can belong to many teams and a team can have many members"""

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=10,
                            choices=Role.choices,
                            default=Role.PLAYER)

    def __str__(self):
        return f"{self.team} - {self.member}"
