import sqlite3 as db

import numpy as np
import pandas as pd


def extractPlayers():
    conn = db.connect('/home/lneeraj97/Documents/mysite/ipl.sqlite3')
    cur = conn.cursor()
    names = ['Player_Id', 'Player_Name', 'Type']
    cur.execute('SELECT Player_Id,Player_Name,Type from Player_Score')
    allPlayers = pd.DataFrame(data=cur.fetchall(), columns=names)
    # print(allPlayers.head(5))
    return allPlayers


def predictSuccess(playerList):
    names = ['Player_Id', 'Avg_Score', 'Success']
    conn = db.connect('/home/lneeraj97/Documents/mysite/ipl.sqlite3')
    cur = conn.cursor()
    args = playerList
    sql = 'SELECT Player_Id, Avg_Score, Success FROM Player_Score WHERE Player_Id IN ({seq})'.format(
        seq=','.join(['?'] * len(args)))
    cur.execute(sql, args)
    teamDF = pd.DataFrame(data=cur.fetchall(), columns=names)
    success = teamDF['Success'].mean()
    score = teamDF['Avg_Score'].mean()
    successRate = 0.8*success + 0.2*score
    return successRate


# extractPlayers()
# predictSuccess([147, 175, 310, 38, 31, 255, 40, 333, 79, 151, 244])
