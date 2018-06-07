import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3 as db
import os
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

dbPath = os.path.join(BASE_DIR, 'ipl.sqlite3')


def getVisualisation(playerId):
    conn = db.connect(dbPath)
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM Player_Match_Complete WHERE Player_Id={pid}'.format(pid=playerId))
    names = [description[0] for description in cur.description]
    playerDF = pd.DataFrame(data=cur.fetchall(), columns=names)
    # playerDF = playerDF.transpose()
    print(playerDF)
    getGraphs(playerDF)


def getGraphs(playerDF):
    playerDF.fillna(0, inplace=True)
    matches = playerDF.index.values
    runs = playerDF['Runs']
    strikeRate = playerDF['Runs'] / playerDF['Bowls_Played']
    wickets = playerDF['Wickets']
    # sns.distplot(runs, bins=10)
    # sns.distplot(wickets, bins=5)
    # runs.plot.hist(bins=200)
    # runs.plot.kde()
    # sns.heatmap(playerDF.corr())
    sns.jointplot(matches, runs, kind='resid')
    plt.show()


getVisualisation(27)
