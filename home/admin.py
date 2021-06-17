from django.contrib import admin
from .models import Players, Teams, Individual_teams, Matches


class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person',
        'current_score',
        'total_goals_for',
        'total_goals_against'
    )

    ordering = ('current_score',)

class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person',
        'team_1',
        'team_2',
        'team_3',
    )

class Individual_teamsAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_team',
        'team_goals_for',
        'team_goals_against',
    )

class MatchesAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person_1',
        'name_of_person_2',
        'team_1',
        'team_2'
    )






admin.site.register(Players, PlayersAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Individual_teams, Individual_teamsAdmin)
admin.site.register(Matches, MatchesAdmin)
