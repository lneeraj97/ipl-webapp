import pandas as pd
import numpy as np
import sqlite3 as db


def getScoresList(playerId):
    conn = db.connect('/home/lneeraj97/Documents/mysite/ipl.sqlite3')
    cur = conn.cursor()
    cur.execute(
        'SELECT Score FROM Player_Match_Score WHERE Player_Id={pid}'.format(pid=playerId))
    names = [description[0] for description in cur.description]
    playerScores = cur.fetchall()
    scores = []
    for item in playerScores:
        scores.append(item[0])
    return scores


# getScoresList(27)
