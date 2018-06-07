import pandas as pd
import numpy as np
import sqlite3 as db
import os
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


def getScoresList(playerId):
    dbPath = os.path.join(BASE_DIR, 'ipl.sqlite3')
    conn = db.connect(dbPath)
    cur = conn.cursor()
    cur.execute(
        'SELECT Score FROM Player_Match_Score WHERE Player_Id={pid}'.format(pid=playerId))
    names = [description[0] for description in cur.description]
    playerScores = cur.fetchall()
    scores = []
    for item in playerScores:
        scores.append(item[0])
    return scores


getScoresList(27)
