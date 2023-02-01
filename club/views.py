from django.shortcuts import render, get_object_or_404
from club.models import Club  # importer le modele pour l'utiliser plus tard
from matches.models import Game
from club.use_cases import get_unique_members, get_games


def index_view(request):
    """Index view welcoming our users
    """
    clubs = Club.objects.all()  # on récupère tous les clubs de notre base
    
    # le contexte est transmis au template
    context = {
        "clubs_list": clubs
    }
    return render(request, "club/index.html", context=context)


def club_detail_view(request, slug):
    """Display important information about a specific club"""
    club = get_object_or_404(Club, slug=slug)
    
    members = get_unique_members(club)

    games = get_games(club)
    
    context = {"club": club, "members_list": members, "teams": club.teams.all(), "team_count": club.teams.count(), "member_count": len(members), "games_list":  games}
    return render(request, "club/detail.html", context=context)
