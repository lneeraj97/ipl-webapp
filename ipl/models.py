# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PlayerMatchComplete(models.Model):
    # Field name made lowercase.
    match_id = models.IntegerField(db_column='Match_Id', blank=True, null=True)
    # Field name made lowercase.blank
    player_id = models.IntegerField(
        db_column='Player_Id', blank=True, null=True)
    # Field name made lowercase.
    team_id = models.IntegerField(db_column='Team_Id', blank=True, null=True)
    # Field name made lowercase.
    batted = models.IntegerField(db_column='Batted', blank=True, null=True)
    # Field name made lowercase.
    bowls_played = models.FloatField(
        db_column='Bowls_Played', blank=True, null=True)
    # Field name made lowercase.
    runs = models.FloatField(db_column='Runs', blank=True, null=True)
    # Field name made lowercase.
    fifties = models.FloatField(db_column='Fifties', blank=True, null=True)
    # Field name made lowercase.
    hundreds = models.FloatField(db_column='Hundreds', blank=True, null=True)
    # Field name made lowercase.
    out = models.FloatField(db_column='Out', blank=True, null=True)
    # Field name made lowercase.
    bowled = models.IntegerField(db_column='Bowled', blank=True, null=True)
    # Field name made lowercase.
    wickets = models.FloatField(db_column='Wickets', blank=True, null=True)
    # Field name made lowercase.
    runs_conceded = models.FloatField(
        db_column='Runs_Conceded', blank=True, null=True)
    # Field name made lowercase.
    overs = models.FloatField(db_column='Overs', blank=True, null=True)
    # Field name made lowercase.
    maiden_overs = models.FloatField(
        db_column='Maiden_Overs', blank=True, null=True)
    # Field name made lowercase.
    extras = models.FloatField(db_column='Extras', blank=True, null=True)
    # Field name made lowercase.
    wickets_as_fielder = models.IntegerField(
        db_column='Wickets_As_Fielder', blank=True, null=True)
    # Field name made lowercase.
    match_won = models.IntegerField(
        db_column='Match_Won', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player_Match_Complete'


class PlayerMatchScore(models.Model):
    # Field name made lowercase.
    match_id = models.FloatField(db_column='Match_Id', blank=True, null=True)
    # Field name made lowercase.
    player_id = models.FloatField(db_column='Player_Id', blank=True, null=True)
    # Field name made lowercase.
    team_id = models.FloatField(db_column='Team_Id', blank=True, null=True)
    # Field name made lowercase.
    is_batsman = models.IntegerField(
        db_column='Is_Batsman', blank=True, null=True)
    # Field name made lowercase.
    is_bowler = models.IntegerField(
        db_column='Is_Bowler', blank=True, null=True)
    # Field name made lowercase.
    is_allrounder = models.IntegerField(
        db_column='Is_Allrounder', blank=True, null=True)
    # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)
    # Field name made lowercase.
    match_won = models.IntegerField(
        db_column='Match_Won', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player_Match_Score'


class PlayerScore(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(
        db_column='Player_Id', blank=True, primary_key=True)
    # Field name made lowercase.
    player_name = models.TextField(
        db_column='Player_Name', blank=True, null=True)
    # Field name made lowercase.
    total_score = models.FloatField(
        db_column='Total_Score', blank=True, null=True)
    # Field name made lowercase.
    avg_score = models.FloatField(db_column='Avg_Score', blank=True, null=True)
    # Field name made lowercase.
    success = models.FloatField(db_column='Success', blank=True, null=True)
    # Field name made lowercase.
    ptype = models.IntegerField(db_column='Type', blank=True, null=True)
    # Field name made lowercase.
    dob = models.TextField(db_column='DOB', blank=True, null=True)
    # Field name made lowercase.
    batting_hand = models.TextField(
        db_column='Batting_Hand', blank=True, null=True)
    # Field name made lowercase.
    bowling_skill = models.TextField(
        db_column='Bowling_Skill', blank=True, null=True)
    # Field name made lowercase.
    overseas = models.IntegerField(db_column='Overseas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player_Score'
