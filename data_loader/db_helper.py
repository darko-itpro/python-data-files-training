#!/usr/bin/env python 

import sqlite3 as sqlite
import re

SQL_CREATE_EPISODES_TABLE = "CREATE TABLE IF NOT EXISTS episodes (number INT NOT NULL, season INT NOT NULL, title TEXT NOT NULL)"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?)"
SQL_GET_ALL_EPISODES = "SELECT title, season, number FROM episodes ORDER BY season, number"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, season, number FROM episodes where season = ? ORDER BY number"


def create_database(dbname="demo"):
    db_name = re.sub("[ .()]", "_", dbname) + '.db'  # Voir regex
    connect = sqlite.connect(db_name)

    try:
        cur = connect.cursor()
        cur.execute(SQL_CREATE_EPISODES_TABLE)

    except sqlite.Error as e:
        print("Error occured")  # Voir docstring pour print
        print(e)  # Voir docstring pour print


def add_episode(title, season_number, number, dbname="demo"):
    import re
    db_name = re.sub("[ .()]", "_", dbname) + '.db'  # Voir regex
    connect = sqlite.connect(db_name)

    cur = connect.cursor()
    cur.execute(SQL_ADD_EPISODE, (number, season_number, title))
    connect.commit()


def load_episodes(season_number=None, dbname="demo"):
    db_name = re.sub("[ .()]", "_", dbname) + '.db'  # Voir regex
    connect = sqlite.connect(db_name)

    cur = connect.cursor()
    if season_number is None:
        cur.execute(SQL_GET_ALL_EPISODES)
    else:
        cur.execute(SQL_GET_EPISODES_FOR_SEASON, (season_number,))
    return cur.fetchall()

