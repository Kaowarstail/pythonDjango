from matches.models import Game
from django.db.models import Q


def get_unique_members(club):
    """Given a club, this will return a list of unique members
    """
    # Nous devons passer sur chaque équipe pour récuperer tous les membres
    members = []
    unique_members = set()
    for team in club.teams.all():
        for memberteam in team.memberteam_set.all():
            members.append(memberteam)
            unique_members.add(memberteam.member.id)

    # On retire les doublons
    members = list(set(members))
    return members


def get_games(club):
    """Given a club will return unique instances of Game
    """
    teams = club.teams.all()
    games_list = Game.objects.filter(
        Q(home_team__in=teams) | Q(away_team__in=teams)
    )
    return games_list