import sqlite3
import pandas as pd conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS Movie_Actor;
CREATE TABLE Movie(
    Movie_Id INTEGER PRIMARY KEY,
    Title    TEXT,
    Genre    Text,
    Year     INTEGER,
    RATING   Real,
    Duration INTEGER
);
CREATE TABLE Movie_Actor(
    Movie_Td INTEGER,
    Actor_Id INTEGER
);
INSERT INTO MOVIE VALUES
(1,'The Lion King','1994,8.5,88),
(2,'Toy Story','Animation',1995,8.3,81),
(3,'Frozen','Animation',2013,7.4,102),
(4,'Moana','Animation',2016,7.6,107),
(5,'Spider-Man','Action',2002,7.3,121),
(12,'Interstellar','Drama',2014,8.6,169);
INSERT INTO Actor VALUES
  (1,'Tom Hanks',1956,'USA')
