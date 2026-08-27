import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("movies.db")

cursor = conn.cursor()

# Create tables and insert data
cursor.executescript("""

DROP TABLE IF EXISTS Movie_Actor;
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Actor;

CREATE TABLE Movie(
    Movie_Id INTEGER PRIMARY KEY,
    Title TEXT,
    Genre TEXT,
    Year INTEGER,
    Rating REAL,
    Duration INTEGER
);

CREATE TABLE Actor(
    Actor_Id INTEGER PRIMARY KEY,
    Actor_Name TEXT,
    Birth_Year INTEGER,
    Country TEXT
);

CREATE TABLE Movie_Actor(
    Movie_Id INTEGER,
    Actor_Id INTEGER
);

INSERT INTO Movie VALUES
(1, 'The Lion King', 'Animation', 1994, 8.5, 88),
(2, 'Toy Story', 'Animation', 1995, 8.3, 81),
(3, 'Frozen', 'Animation', 2013, 7.4, 102),
(4, 'Moana', 'Animation', 2016, 7.6, 107),
(5, 'Spider-Man', 'Action', 2002, 7.3, 121),
(12, 'Interstellar', 'Drama', 2014, 8.6, 169);

INSERT INTO Actor VALUES
(1, 'Tom Hanks', 1956, 'USA'),
(2, 'Idris Elba', 1972, 'UK'),
(3, 'Chadwick Boseman', 1976, 'USA'),
(4, 'Scarlett Johnson', 1984, 'USA'),
(5, 'Macaulay Culkin', 1980, 'USA');

INSERT INTO Movie_Actor VALUES
(1, 2),
(2, 1),
(5, 1),
(12, 3),
(12, 1);

""")

conn.commit()

print("Database ready!")

# 1. Get unique genres
genres = pd.read_sql("""
SELECT DISTINCT Genre
FROM Movie;
""", conn)

print("\nGenres:")
print(genres)


# 2. Get unique countries
countries = pd.read_sql("""
SELECT DISTINCT Country
FROM Actor;
""", conn)

print("\nCountries:")
print(countries)


# 3. Movies sorted by rating
top_movies = pd.read_sql("""
SELECT Title, Genre, Rating
FROM Movie
ORDER BY Rating DESC;
""", conn)

print("\nMovies by Rating:")
print(top_movies)


# 4. Movies from oldest to newest
oldest_first = pd.read_sql("""
SELECT Title, Year
FROM Movie
ORDER BY Year ASC;
""", conn)

print("\nMovies from Oldest to Newest:")
print(oldest_first)


# 5. Actors from youngest to oldest
youngest_actors = pd.read_sql("""
SELECT Actor_Name, Birth_Year, Country
FROM Actor
ORDER BY Birth_Year DESC;
""", conn)

print("\nYoungest Actors:")
print(youngest_actors)


# 6. Count Action movies
action_count = pd.read_sql("""
SELECT COUNT(Movie_Id) AS Action_Movie_Count
FROM Movie
WHERE Genre = 'Action';
""", conn)

print("\nNumber of Action Movies:")
print(action_count)


# 7. Total duration of Animation movies
animation_mins = pd.read_sql("""
SELECT SUM(Duration) AS Total_Animation_Duration
FROM Movie
WHERE Genre = 'Animation';
""", conn)

print("\nTotal Duration of Animation Movies:")
print(animation_mins)


# Close database connection
conn.close()
