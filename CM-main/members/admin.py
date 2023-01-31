from django.contrib import admin

from members.models import Member, Team, MemberTeam

class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "club")

admin.site.register(Member)
admin.site.register(Team, TeamAdmin)
admin.site.register(MemberTeam)