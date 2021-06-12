from django.contrib import admin
from .models import Players, Teams


class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person',
        'current_score',
    )

    ordering = ('current_score',)

class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person',
        'team_1',
        'team_2',
        'team_3',
    )

    ordering = ('current_score',)





admin.site.register(Players, PlayersAdmin)
admin.site.register(Players, TeamsAdmin)
