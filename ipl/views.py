import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from .code.mainCode import getPlayers, pickPlayers, selectPlayers
from .forms import InputForm, OptionsForm
from .models import PlayerMatchComplete, PlayerMatchScore, PlayerScore
from .code.altPlayers import getAltPlayer
from .code.predict import extractPlayers, predictSuccess
from .code.graphsdata import getScoresList

# import sqlite3 as db
# import numpy as np
# from django_tables2.tables import Table
# Create your views here.


# Home page view
def home(request):
    return render(request, 'home.html')


# View that takes in user requirements
def input(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            request.session['success'] = form.cleaned_data['success']
            request.session['batsmen'] = form.cleaned_data['batsmen']
            request.session['bowlers'] = form.cleaned_data['bowlers']
            request.session['allrounders'] = form.cleaned_data['allrounders']
            request.session['foreignBatsmen'] = form.cleaned_data['foreignBatsmen']
            request.session['foreignBowlers'] = form.cleaned_data['foreignBowlers']
            request.session['foreignAllrounders'] = form.cleaned_data['foreignAllrounders']
            return HttpResponseRedirect('output')
        else:
            form = InputForm()

    else:
        form = InputForm()
    return render(request, 'input.html', {'form': form})


# View that selects the team and outputs it
def output(request):
    success = request.session['success']
    batsmen = request.session['batsmen']
    bowlers = request.session['bowlers']
    allrounders = request.session['allrounders']
    foreignBatsmen = request.session['foreignBatsmen']
    foreignBowlers = request.session['foreignBowlers']
    foreignAllrounders = request.session['foreignAllrounders']

    req = {'Success': success, 'Bat': batsmen, 'Bowl': bowlers,
           'Allr': allrounders, 'fBat': foreignBatsmen, 'fBowl': foreignBowlers, 'fAll': foreignAllrounders}
    players = getPlayers(req)

    request.session['playerTable'] = players['Player_Id'].tolist()
    # print(request.session.get('playerTable'))
    return render(request, 'output.html', {'playerTable': players})


def alternatives(request):
    playerList = request.session['playerTable']
    altPlayerList = []
    for item in playerList:
        altPlayerList.append(getAltPlayer(playerList, item).reset_index().head(
            5)[['Player_Id', 'Player_Name', 'Success']])
    # print(altPlayerList)
    mylist = zip(playerList, altPlayerList)
    return render(request, 'alternatives.html', {'mylist': mylist})


# View that predicts the success for a given team


def options(request):
    playersDF = extractPlayers()
    # print(playersDF.head(5))
    return render(request, 'options.html', {'playersDF': playersDF})


def predict(request):
    playerIds = request.POST.get('pickedPlayers').split(',')
    # print(playerIds)
    success = predictSuccess(playerIds)
    request.session['playerTable'] = playerIds
    # messages.info(
    # request, "The probability of your team's success is {0} %".format(success))
    return render(request, 'success.html', {'success': success})


def charts(request):
    playerList = request.session['playerTable']
    reqData = getScoresList(playerList)
    return render(request, 'charts.html', {'mydata': reqData})
