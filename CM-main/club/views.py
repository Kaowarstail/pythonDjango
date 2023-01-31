from django.shortcuts import render, get_object_or_404
from club.models import Club  # importer le modele pour l'utiliser plus tard


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

    # Nous devons passer sur chaque équipe pour récuperer tous les membres
    members = []
    unique_members = set()
    for team in club.teams.all():
        for memberteam in team.memberteam_set.all():
            members.append(memberteam)
            unique_members.add(memberteam.member.id)

    # On retire les doublons
    members = list(set(members))
    
    context = {"club": club, "members_list": members, "teams": club.teams.all(), "team_count": club.teams.count(), "member_count": len(unique_members)}
    return render(request, "club/detail.html", context=context)
