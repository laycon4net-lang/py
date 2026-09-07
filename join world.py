import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE author (
)""")
conn.execute("""CREATE TABLE book (
    book_id    INTEGER PRIMARY KEY,
    book_title TEXT NOT NULL,
    author_id INTEGER
)""")
conn.executemany("INSERT INTO author VALUES (?, ?)", [
    (1, 'Roald Dahl'),
    (2, 'J.k Rowling'),
    (3, 'Rick Riordan'),
    (4, 'Jeff kinnery'),
    (5, 'Dav pilkey'),
    (6, 'Lemomy snicket'),
])
conn.executemany("INSERT INTO book VALUES (?, ?, ?)",[
    (1, 'Charlie and the Chocolate Factory',        1),
    (2, 'James and the Giant Peach',                2),
    (3, 'Harry potter and the Philosphers Stone',   3),
    (4, 'Harry potter and the Chamber of Secrets',  4),
    (5, 'The Lightning Theif',                      5),
    (6, 'The Sea of Monsters',                      6),
    (7, 'Diary of a wimpy kid',)
])
conn.commit()
authors = pd.read_sql("SELECT * FROM author", conn)
books = pd.read_sql("SELECT * FROM book", conn)
print("Author table:")
print(authors)
print()
print("Book table:")
print(books)
print()