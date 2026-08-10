CREATE  TABLE IF NOT EXISTS Resturant (
    name TEXT,
    neighborhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);
INSERT INTO Resturant (name, neighborhood, cuisine, review, price, health)
VALUES
('peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');
SELECT DISTINCT neighborhood
FROM Restaurant;
SELECT DISTINCT cuisine = 'Chinese';
SELECT *
FROM Restaurant
WHERE review >=4.0;
SELECT *
FROM Restaurant
WHERE price = '$$$';
SELECT *
FROM RESTURANT
WHERE NAME LIKE '%Candy%';
SELECT *
FROM Restaurant
WHERE neighborhood IN ('Midtown', 'Downtown', 'Chinatown');
SELECT *
FROM Restaurant
ORDER BY review DESC
LIMIT 4;
