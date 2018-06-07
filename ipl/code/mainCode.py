import sqlite3 as db

import numpy as np
import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

dbPath = os.path.join(BASE_DIR, 'ipl.sqlite3')


def pickPlayers(playerList, numOfPlayers, finalTeam):
    while numOfPlayers > 0:
        if numOfPlayers != 0:
            finalTeam = finalTeam.append(playerList.head(1))
            playerList = playerList.iloc[1:]
            numOfPlayers -= 1
        if numOfPlayers != 0:
            finalTeam = finalTeam.append(playerList.tail(1))
            playerList = playerList.iloc[:-1]
            numOfPlayers -= 1

    return finalTeam


def getRequirements():

    # Asks the user inputs for the success rate, number of batsmen, bowlers and allrounders needed
    # Returns a dictionary with the following keys: Success, Batsmen, Bowlers, Allrounders

    successRate = input("Enter the success rate you want (1-60) :")
    try:
        successRate = float(successRate)
    except ValueError:
        print('Invalid Input')
        pass

    batsmen = input('Enter the number of batsmen you want :')
    try:
        batsmen = int(batsmen)
    except ValueError:
        print('Invalid Input')
        pass
    bowlers = input('Enter the number of bowlers you want :')
    try:
        bowlers = int(bowlers)
    except ValueError:
        print('Invalid Input')
        pass
    allrounders = input('Enter the number of Allrounders you want :')
    try:
        allrounders = int(allrounders)
    except ValueError:
        print('Invalid Input')
        pass
    requirements = {'Success': successRate, 'Batsmen': batsmen,
                    'Bowlers': bowlers, 'Allrounders': allrounders}
    return requirements


def getPlayers(requirements):
    success = requirements['Success']
    num_bat = requirements['Bat']
    num_bowl = requirements['Bowl']
    num_all = requirements['Allr']
    num_fBat = requirements['fBat']
    num_fBowl = requirements['fBowl']
    num_fAll = requirements['fAll']
    num_iBat = num_bat - num_fBat
    num_iBowl = num_bowl - num_fBowl
    num_iAll = num_all - num_fAll
    indian = 0
    foreign = 1
    batsmen = 1
    bowler = 2
    allrounder = 3
    names = ['Player_Id', 'Player_Name', 'Total_Score', 'Avg_Score',
             'Success', 'Type', 'DOB', 'Batting_Hand', 'Bowling_Skill', 'Overseas']
    finalTeam = pd.DataFrame(columns=names)
    # Foreifn Allrounders
    finalTeam = selectPlayers(num_fAll, allrounder,
                              foreign, success, finalTeam)
    finalTeam = selectPlayers(num_fBat, batsmen, foreign, success, finalTeam)
    finalTeam = selectPlayers(num_fBowl, bowler, foreign, success, finalTeam)
    finalTeam = selectPlayers(num_iAll, allrounder, indian, success, finalTeam)
    finalTeam = selectPlayers(num_iBat, batsmen, indian, success, finalTeam)
    finalTeam = selectPlayers(num_iBowl, bowler, indian, success, finalTeam)
    finalTeam.drop_duplicates(inplace=True)
    finalTeam.reset_index(inplace=True)
    finalTeam.drop('index', axis=1, inplace=True)
    return finalTeam


def selectPlayers(num, ptype, overseas, success, finalTeam):
    new_success = success
    successMin = success - 2
    successMax = success + 2

    # Open the database
    try:
        conn = db.connect(dbPath)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Player_Score WHERE (Total_Score>200 AND Success BETWEEN {0} AND {1}) AND Type={2} AND Overseas={3} ORDER BY Total_Score DESC,Success DESC ".format(
            successMin, successMax, ptype, overseas))
        players = pd.DataFrame(data=cur.fetchall(), columns=finalTeam.columns)
        # print(players)
        if len(players) < num:
            if success >= 60:
                new_success = new_success - 5
            else:
                new_success = new_success + 5
            finalTeam = selectPlayers(
                num, ptype, overseas, new_success, finalTeam)
            return finalTeam
        finalTeam = pickPlayers(players, num, finalTeam)
        # print(finalTeam)
    except:
        pass

    return finalTeam


req = {'Success': 53, 'Bat': 5, 'Bowl': 3,
       'Allr': 3, 'fBat': 0, 'fBowl': 2, 'fAll': 2}
players = getPlayers(req)
# print(players)
# players.to_html('./playerTable.html')
