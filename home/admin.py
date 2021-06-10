from django.contrib import admin
from .models import Players


class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_person',
        'current_score',
    )

    ordering = ('current_score',)





admin.site.register(Players, PlayersAdmin)
