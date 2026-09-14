import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute("CREATE TABLE recepie (recepie_id INTEGER PRIMARY KEY, recepie_name TEXT" 
"NOT NULL, cuisine TEXT NOT NULL, prep_miss INTEGER NOT NULL)")
conn.execute("CREATE TABLE ingridient (ingridient_id INTEGER PRIMARY KEY, recepie_id INTEGER NOT NULL, item TEXT NOT NULL, quantity_g INTEGER NOT NULL)")
conn.executemany("INSERT INTO recepie VALUES (?, ?, ?, ?)",[
    (1,'pasta', 'italian', 20),
    (2,'Tacos', 'Mexican', 15),
    (3,'Sushi', 'Japanes', 45),
    (4,'pizza', 'Italian', 30),
    (5,'Salad', 'Greek',   10),
])
conn.executemany("Insert INTO ingridents VALUES (?, ?, ?, ?)",[
    (1,1, 'Pasta')
])
