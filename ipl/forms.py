from django import forms
from .models import PlayerScore


class InputForm(forms.Form):
    batsmen = forms.IntegerField(min_value=0, max_value=7)
    bowlers = forms.IntegerField(min_value=0, max_value=7)
    allrounders = forms.IntegerField(min_value=0, max_value=7)
    foreignBatsmen = forms.IntegerField(min_value=0, max_value=4)
    foreignBowlers = forms.IntegerField(min_value=0, max_value=4)
    foreignAllrounders = forms.IntegerField(min_value=0, max_value=4)
    success = forms.FloatField(min_value=0, max_value=100, required=True)


class OptionsForm(forms.Form):
    playerIds = forms.CharField(widget=forms.Textarea(
        attrs={'cols': "50", 'rows': "20"}))
