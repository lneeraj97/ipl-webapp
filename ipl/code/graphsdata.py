import pandas as pd
import numpy as np
import sqlite3 as db
import os


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


def getScoresList(playersList):
    dbPath = os.path.join(BASE_DIR, 'ipl.sqlite3')
    conn = db.connect(dbPath)
    cur = conn.cursor()
    result = [['null' for i in range(len(playersList)+1)]
              for l in range(0, 150)]
    for i in range(1, 151):
        result[i-1][0] = i
    for i in range(1, len(playersList)):
        playerId = playersList[i]
        cur.execute(
            'SELECT Score FROM Player_Match_Score WHERE Player_Id={pid}'.format(pid=playerId))
        playerScores = cur.fetchall()
        # print(len(playerScores))
        for j in range(len(playerScores)):
            result[j][i] = playerScores[j][0]
    indices = ['Match', 'Player1', 'Player2', 'Player3', 'Player4', 'Player5',
               'Player6', 'Player7', 'Player8', 'Player9', 'Player10', 'Player11']
    result.insert(0, indices)
    return result


# sc = getScoresList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# print(sc)
