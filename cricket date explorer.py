import pandas as pd
import sqlite3
conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;
CREATE TABLE Team;
    Team_ID   INTEGER PRIMARY KEY,
    Team_Name Text
);
CREATE TABLE Match(
    Match_Id     INTEGER PRIMARY KEY,
    season_Id    INTEGER,
    Match_Winner Integer,
    Win_Maargin  Integer)
);
CREATE TABLE Player_Match(
    Match_Id  INTEGER,
    Player_Id Integer
);
CREATE TABLE Player_Match(
    Match_Id  INTEGER,
    player_Id INTEGER
);
INSERT INTO TEAM VALUES
(1,'Chennai Super Kings'),(2,'Delhi Capitals'),
(3,'Deccan Chargers'),(4,'Delhi Daredevils'),
(5,'Mumbai INDIANS'),(6,'Kolkata knight Riders'),
(7,"Rajasthan Royals'),(8,'kinght XI punjab');
(1,7,5,35),(2,7,5,22),(3,8,5,45),(4,8,5,8),
(5,8,1,67),(6,8,6,19),()