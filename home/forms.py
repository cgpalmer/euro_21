from django import forms
from .models import Players, Matches, Individual_teams, Teams


class MatchesForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = '__all__'

class KnockoutForm(forms.ModelForm):
    class Meta:
        model = Individual_teams
        fields = '__all__'