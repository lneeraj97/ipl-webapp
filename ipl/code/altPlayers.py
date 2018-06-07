import sqlite3 as db

import numpy as np
import pandas as pd


def getAltPlayer(playerList, playerId):
    altFor = playerId
    # Open Database
    conn = db.connect('/home/lneeraj97/Documents/mysite/ipl.sqlite3')
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM Player_Score WHERE Player_Id={pid}'.format(pid=altFor))
    names = [description[0] for description in cur.description]
    playerDF = pd.DataFrame(data=cur.fetchall(), columns=names)
    # print(playerDF)
    pType = playerDF['Type']
    pType = pType.iloc[0]
    overseas = playerDF['Overseas']
    overseas = overseas.iloc[0]
    pSuccess = playerDF['Success']
    pSuccess = pSuccess.iloc[0]
    sMin = pSuccess - 5
    sMax = pSuccess + 5
    args = playerList
    sql = 'SELECT * FROM Player_Score WHERE Total_Score>200 AND Player_Id NOT IN ({seq})'.format(
        seq=','.join(['?']*len(args)))
    cur.execute(sql, args)
    altPlayersList = pd.DataFrame(data=cur.fetchall(), columns=names)
    if len(altPlayersList) == 0:
        return "No Alternate Players in this range"
    sameType = altPlayersList['Type'] == pType
    sameOS = altPlayersList['Overseas'] == overseas
    sameSuccess = (altPlayersList['Success'] < sMax) & (
        altPlayersList['Success'] > sMin)
    altPlayersList = altPlayersList[sameOS & sameType & sameSuccess]
    return altPlayersList


players = [147, 175, 310, 38, 31, 255, 40, 333, 79, 151, 244]
output = []
for item in players:
    output.append(getAltPlayer(players, item).head(5))
# print(output)
