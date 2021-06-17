from django.db import models

# Create your models here.
from django.db import models

class Players(models.Model):
    name_of_person = models.CharField(max_length=254, null=True, blank=True)
    current_score = models.IntegerField(null=True, blank=True)
    total_goals_for = models.IntegerField(null=True, blank=True)
    total_goals_against = models.IntegerField(null=True, blank=True)
   
    def __str__(self):
        return self.name_of_person

class Teams(models.Model):
    name_of_person = models.CharField(max_length=254, null=True, blank=True)
    team_1 = models.CharField(max_length=254, null=True, blank=True)
    team_2 = models.CharField(max_length=254, null=True, blank=True)
    team_3 = models.CharField(max_length=254, null=True, blank=True)
    auto_team_1 = models.ForeignKey('Individual_teams', null=True, blank=True, on_delete=models.SET_NULL, related_name="player_team_1")
    auto_team_2 = models.ForeignKey('Individual_teams', null=True, blank=True, on_delete=models.SET_NULL, related_name="player_team_2")
    auto_team_3 = models.ForeignKey('Individual_teams', null=True, blank=True, on_delete=models.SET_NULL, related_name="player_team_3")

   
    def __str__(self):
        return self.name_of_person



class Matches(models.Model):
    name_of_person_1 = models.ForeignKey('Players', null=True, blank=True, on_delete=models.SET_NULL, related_name="Player_1")
    name_of_person_2 = models.ForeignKey('Players', null=True, blank=True, on_delete=models.SET_NULL, related_name="Player_2")
    team_1 = models.ForeignKey('Individual_teams', null=True, blank=True, on_delete=models.SET_NULL, related_name="team_1")
    team_2 = models.ForeignKey('Individual_teams', null=True, blank=True, on_delete=models.SET_NULL, related_name="team_2")
    team_1_goals = models.IntegerField(null=True, blank=True, default=0)
    team_2_goals = models.IntegerField(null=True, blank=True, default=0)
    team_1_score = models.IntegerField(null=True, blank=True, default=0)
    team_2_score = models.IntegerField(null=True, blank=True, default=0)
    team_1_red_card = models.IntegerField(null=True, blank=True, default=0)
    team_2_red_card = models.IntegerField(null=True, blank=True, default=0)
    team_1_win_rival = models.BooleanField()
    team_2_win_rival = models.BooleanField()
    team_1_draw_rival = models.BooleanField()
    team_2_draw_rival = models.BooleanField()
   
    def __str__(self):
        return self.name_of_person


class Individual_teams(models.Model):
    name_of_team = models.CharField(max_length=254, null=True, blank=True)
    team_goals_for = models.IntegerField(null=True, blank=True, default=0)
    team_goals_against = models.IntegerField(null=True, blank=True, default=0)
    team_knocked_out_groups = models.BooleanField(default=False)
    team_knocked_out = models.BooleanField(default=False)


    def __str__(self):
        return self.name_of_team

