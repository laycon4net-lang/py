CREATE TABLE IF NOT EXISTS BOOK (
    book_id  INTEGER PRIMARY KEY,
    title    TEXT    NOT NULL,
    genre    TEXT    NOT NULL,
    rating   REAL    NOT NULL,
    pages    INTEGER NOT NULL,
    pub_year INTEGER NOT NULL
);
INSERT INTO BOOK VALUES (1, 'Dragon Quest',    'fantansy',  9.2, 312, 2021);
INSERT INTO BOOK VALUES (2, 'Code Wizards',    'Sci-Fi',    8.5, 280, 2020);
INSERT INTO BOOK VALUES (3, 'Ocean Deep',      'Adventure', 7.8, 195, 2022);
INSERT INTO BOOK VALUES (4, 'Star Rangers',    'Sci-Fi',    9.5, 340, 2019);
INSERT INTO BOOK VALUES (5, 'Forest Secrets',  'Fatansy',   8.1, 228, 2023);
INSERT INTO BOOK VALUES (6, 'Robot City',      'Sci-Fi',    7.2, 260, 2021);
INSERT INTO BOOK VALUES (7, 'Time Jumpers',    'Adventure', 8.9, 175, 2022);
INSERT INTO BOOK VALUES (8, 'Magic Academy',   'Fantasy',   9.0, 398, 2020);
SELECT * FROM BOOK;
SELECT title, rating FROM book ORDER BY rating ASC;