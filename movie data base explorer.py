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
  (1,'Tom Hanks',1956,'USA'),
  (2,'Idris Elba',1972,'UK'),
  (3,'Chadwick Boseman',1976,'USA'),
  (4,'Scarlettt Johnson',1984,'1984,'USA')
  (5,'Macaulay Culkin',1980,'USA'),
  INSERT INTO Movie_Actor VALUES
  (1,2),(2,1),(5,1),(6,3),(6,8),(7,4),(8,7),(9,5),(11,2),(12,1);
  """)
conn.commit()
print('Database ready!')
  
