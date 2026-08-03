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
INSERT INTO Customer (customer_id,cust_name,city,grade,Salesman_id)
VALUES
("3002","nick rimando","new york","100","5001"),
("3007", "brad davis", "new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabiam johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"),
("3001","brad guzan","london","","5005");
CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    Purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT,
);
INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,Salesman_id)
VALUES
  ("70001","150.5","2012-10-05","3005","5002"),
  ("70009","270.65","2012-09-10","3001","5001"),
  ("70002","65.26","2012-10-05","3002","5003"),
  ("70004","110.5","2012-08-17","3009","5007"),
  ("70007","948.5","2012-09-10","3005","5005"),
  ("70005","2400.6","2012-07-27","3007","5006");
  --Queries
  --Matchingcustomers and Salesman by city
  SELECT customer.cust_name, Salesman.name, Salesman.city
  FROM Customer
  JOIN Salesman ON Customer.city = Salesman.city;
  SELECT Customer.cust_name, Salesman.name
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id;
SELECT Orders.ord_no, Customer.cust_name, Orders.Salesman_id
FROM Orders
JOIN 
