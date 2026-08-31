import sqlite3
import pandas as pd
conn = sqlite3.connect('cities.db')
conn.execute("DROP TABLE IS EXISTS City;")
conn.execute("""
CREATE TABLE City (
CityId INTEGER    PRIMARY KEY,
City_Name TEXT    NOT NULL UNIQUE,
Country   TEXT    NOT NULL,
Population INTEGER,
IS_Capital TEXT  DEFAULT 'No'
conn.execute("INSERT INTO Cit))y VALUES (1, 'Tokyo',   'Japan',   13960000, 'Yes');")
conn.execute("INSERT INTO City VALUES (2 'Nairobi', 'Kenya', 4397000, 'yes');")
conn.execute('INSERT INTO City VALUES (3, 'Mumbai', 'India',    20667656, 'No');")
conn.execute("INSERT INTO City VALUES (4, 'Sao paulo', 'Brazil', 12325232, 'No');")
conn.execute("INSERT INTO City (City_Id, city_Name, Country) Values (6, 'Sydney',
'Australia');")
print('Rows inserted succesfully!")
cities = pd.read_sql("SELECT * FROM City)
)