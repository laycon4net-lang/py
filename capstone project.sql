CREATE TABLE IF NOT EXISTS Salesman(
Salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
Comission TEXT
);
INSERT INTO Salesman(Salesman_id,name,city, comission)
VALUES
("5001","James Hoog","New Work","0.15"),
("5001","Nail knite","paris","0.13"),
("5005","pit Alex","London", "0.11"),
("5006","Mc Lyon","paris","0.14"),
("5007","paul Adam","Rome","0.13"),
("5003","Lauson Hen","San Jose","0.12");
CREATE TABLE IF NOT EXISTS Customer(
    customer_id TEXT,
    cust_name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT
);
INSERT INTO CUSTERMER(customer_id,cust_name,city,grade,Salesman_id)
VALUES
("3002","nick rimando","new york","100","5001"),
("3007", "brad davis", "new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabiam johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"),
("3001",)
