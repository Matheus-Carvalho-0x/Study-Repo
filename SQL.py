# SQL stands for Structured Query Language
# SQL lets you access and manipulate databases
# SQL became a standard of the American National Standards Institute (ANSI) in 1986, and
# of the International Organization for Standardization (ISO) in 1987
"""
What Can SQL do?
SQL can execute queries against a database
SQL can retrieve data from a database
SQL can insert records in a database
SQL can update records in a database
SQL can delete records from a database
SQL can create new databases
SQL can create new tables in a database
SQL can create stored procedures in a database
SQL can create views in a database
SQL can set permissions on tables, procedures, and views
"""
# Although SQL is an ANSI/ISO standard, there are different versions of the SQL language.
# However, to be compliant with the ANSI standard, they all support at least the major commands
# (such as SELECT, UPDATE, DELETE, INSERT, WHERE) in a similar manner.
"""
To build a web site that shows data from a database, you will need:

An RDBMS database program (i.e. MS Access, SQL Server, MySQL)
To use a server-side scripting language, like PHP or ASP
To use SQL to get the data you want
To use HTML / CSS to style the page
"""
"""
RDBMS

RDBMS stands for Relational Database Management System.

RDBMS is the basis for SQL, and for all modern database systems such as MS SQL Server, 
IBM DB2, Oracle, MySQL, and Microsoft Access.

The data in RDBMS is stored in database objects called tables. A table is a collection of related data entries 
and it consists of columns and rows.
"""
# A database most often contains one or more tables. Each table is identified by a name (e.g. "Customers" or "Orders"),
# and contain records (rows) with data.
# NOTE: SQL keywords are NOT case sensitive: select is the same as SELECT
# Some database systems require a semicolon at the end of each SQL statement.
# Semicolon is the standard way to separate each SQL statement in database systems that allow more than one SQL statement
#  to be executed in the same call to the server.
"""
Some of The Most Important SQL Commands
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index
"""

# ===========================================================================================================================
"""
NOTE: Did you notice that we did not insert any number into the CustomerID field?
The CustomerID column is an auto-increment field and will be generated automatically when a new record is 
inserted into the table.

It's common that the id field is incremented automatically
"""

# SELECT
# The SELECT statement is used to select data from a database.
# e.g SELECT CustomerName, City FROM Customers;
"""
SELECT column1, column2, ...
FROM table_name;
"""
# e.g SELECT * FROM Customers;  (select all data from that table)


# SELECT DISTINCT
# The SELECT DISTINCT statement is used to return only distinct (different) values.
# e.g SELECT DISTINCT Country FROM Customers;
# Inside a table, a column often contains many duplicate values; and sometimes
#  you only want to list the different (distinct) values.
# (So basically is like selecting all and then turn all into a set so the duplicates are ignored)
"""
SELECT DISTINCT column1, column2, ...
FROM table_name;
"""


# WHERE
# The WHERE clause is used to filter records.
# It is used to extract only those records that fulfill a specified condition.
# e.g SELECT * FROM Customers WHERE Country='Mexico';
"""
SELECT column1, column2, ...
FROM table_name
WHERE condition;
"""
# SQL requires single quotes around text values (most database systems will also allow double quotes).
# However, numeric fields should not be enclosed in quotes
# e.g SELECT * FROM Customers WHERE CustomerID=1;
# NOTE: You can use other operators than the = operator to filter the search.
# e.g SELECT * FROM Customers WHERE CustomerID > 80;
"""
Operator	Description	
=	Equal	
>	Greater than	
<	Less than	
>=	Greater than or equal	
<=	Less than or equal	
<>	Not equal. Note: In some versions of SQL this operator may be written as !=	
BETWEEN	Between a certain range	
LIKE	Search for a pattern	
IN	To specify multiple possible values for a column
"""


# ORDER BY
# The ORDER BY keyword is used to sort the result-set in ascending or descending order.
# e.g SELECT * FROM Products ORDER BY Price;
"""
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
"""
# The ORDER BY keyword sorts the records in ascending order by default. To sort the records
# in descending order, use the DESC keyword.
# e.g SELECT * FROM Products ORDER BY Price DESC;
# For string values the ORDER BY keyword will order alphabetically
# e.g SELECT * FROM Products ORDER BY ProductName;
# The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and
# the "CustomerName" column. This means that it orders by Country, but if some rows have the same Country, it
# orders them by CustomerName:
# e.g SELECT * FROM Customers ORDER BY Country, CustomerName;
# The following SQL statement selects all customers from the "Customers" table, sorted ascending by the "Country" and
# descending by the "CustomerName" column:
# e.g SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;


# AND
# The WHERE clause can contain one or many AND operators.
# The AND operator is used to filter records based on more than one condition, like if you want to return all customers from
# Spain that starts with the letter 'G':
# e.g SELECT * FROM Customers WHERE Country = 'Spain' AND CustomerName LIKE 'G%';
"""
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
"""
# You can combine the AND and OR operators.
# The following SQL statement selects all customers from Spain that starts with a "G" or an "R".
# Make sure you use parenthesis to get the correct result.
# e.g SELECT * FROM Customers WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');
# Without parenthesis, the select statement will return all customers from Spain that starts with a "G", plus all
#  customers that starts with an "R", regardless of the country value


# NOT
# The NOT operator is used in combination with other operators to give the opposite result, also called the negative result.
# In the select statement below we want to return all customers that are NOT from Spain:
# e.g SELECT * FROM Customers WHERE NOT Country = 'Spain';
"""
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
"""
# Select customers that does not start with the letter 'A':
# e.g SELECT * FROM Customers WHERE CustomerName NOT LIKE 'A%';
# Select customers with a customerID not between 10 and 60:
# e.g SELECT * FROM Customers WHERE CustomerID NOT BETWEEN 10 AND 60;
# Select customers that are not from Paris or London:
# e.g SELECT * FROM Customers WHERE City NOT IN ('Paris', 'London');
# Select customers with a CustomerId not greater than 50:
# e.g SELECT * FROM Customers WHERE NOT CustomerID > 50;


# INSERT INTO
# The INSERT INTO statement is used to insert new records in a table.
# NOTE: It is possible to write the INSERT INTO statement in two ways:
# 1. Specify both the column names and the values to be inserted:
"""
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
"""
# 2. If you are adding values for all the columns of the table, you do not need to specify the column names in
# the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here,
# the INSERT INTO syntax would be as follows:
"""
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
"""
# (So basically, if you will add a totally new entry then the 2nd one otherwise the 1st one)
# The following SQL statement inserts a new record in the "Customers" table:
# e.g INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
#     VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
# It is also possible to only insert data in specific columns.
# The following SQL statement will insert a new record, but only insert data in the "CustomerName",
# "City", and "Country" columns:
# e.g INSERT INTO Customers (CustomerName, City, Country) VALUES ('Cardinal', 'Stavanger', 'Norway');
# NOTE: The remaining fields will have a "null" value
# It is also possible to insert multiple rows in one statement.
# To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:
# e.g INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
#     VALUES
#     ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
#     ('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
#     ('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
# NOTE: Make sure you separate each set of values with a comma ,


# NULL
# A field with a NULL value is a field with no value.
# If a field in a table is optional, it is possible to insert a new record or update a record without adding
# a value to this field. Then, the field will be saved with a NULL value.
# Note: A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value
# is one that has been left blank during record creation!
# NOTE: It is not possible to test for NULL values with comparison operators, such as =, <, or <>.
# We will have to use the IS NULL and IS NOT NULL operators instead.
"""
The IS NULL operator is used to test for empty values (NULL values).

SELECT column_names
FROM table_name
WHERE column_name IS NULL;

The IS NOT NULL operator is used to test for non-empty values (NOT NULL values).

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
"""
# The following SQL lists all customers with a NULL value in the "Address" field:
# e.g SELECT CustomerName, ContactName, Address FROM Customers WHERE Address IS NULL;
# The following SQL lists all customers with a value in the "Address" field:
# e.g SELECT CustomerName, ContactName, Address FROM Customers WHERE Address IS NOT NULL;


# UPDATE
# The UPDATE statement is used to modify the existing records in a table.
"""
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
"""
# NOTE: Be careful when updating records in a table! Notice the WHERE clause in the UPDATE statement.
# The WHERE clause specifies which record(s) that should be updated. If you omit the WHERE clause, all records
#  in the table will be updated!
# NOTE: NÃO FAZER UPDATE OU DELETE SEM WHERE!
# The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city:
# e.g UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;
# It is the WHERE clause that determines how many records will be updated.
# The following SQL statement will update the ContactName to "Juan" for all records where country is "Mexico":


# DELETE
# The DELETE statement is used to delete existing records in a table.
"""
DELETE FROM table_name WHERE condition;
"""
# The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:
# e.g DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
# It is possible to delete all rows in a table without deleting the table. This means that the table
# structure, attributes, and indexes will be intact:
"""
DELETE FROM table_name;
"""
# To delete the table completely, use the DROP TABLE statement:
# e.g DROP TABLE Customers;


# SELECT TOP
# The SELECT TOP clause is used to specify the number of records to return.
# The SELECT TOP clause is useful on large tables with thousands of records. Returning a large number
#  of records can impact performance.
# Select only the first 3 records of the Customers table:
# e.g SELECT TOP 3 * FROM Customers;
# NOTE: Not all database systems support the SELECT TOP clause. MySQL supports the LIMIT clause to select
# a limited number of records, while Oracle uses FETCH FIRST n ROWS ONLY and ROWNUM.
"""
*SQL Server / MS Access Syntax:

SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

*MySQL Syntax:

SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

*Oracle 12 Syntax:

SELECT column_name(s)
FROM table_name
ORDER BY column_name(s)
FETCH FIRST number ROWS ONLY;

*Older Oracle Syntax:

SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;

*Older Oracle Syntax (with ORDER BY):

SELECT *
FROM (SELECT column_name(s) FROM table_name ORDER BY column_name(s))
WHERE ROWNUM <= number;
"""
# The following SQL statement selects the first 50% of the records from the "Customers" table (for SQL Server/MS Access):
# e.g SELECT TOP 50 PERCENT * FROM Customers;
# The following SQL statement shows the equivalent example for Oracle:
# e.g SELECT * FROM Customers FETCH FIRST 50 PERCENT ROWS ONLY;
# The following SQL statement selects the first three records from the "Customers" table, where the country
# is "Germany" (for SQL Server/MS Access):
# e.g SELECT TOP 3 * FROM Customers WHERE Country='Germany';
# The following SQL statement shows the equivalent example for MySQL:
# e.g SELECT * FROM Customers WHERE Country='Germany' LIMIT 3;
# The following SQL statement shows the equivalent example for Oracle:
# e.g SELECT * FROM Customers WHERE Country='Germany' FETCH FIRST 3 ROWS ONLY;
# Add the ORDER BY keyword when you want to sort the result, and return the first 3 records of the sorted result.
# For SQL Server and MS Access:
# e.g SELECT TOP 3 * FROM Customers ORDER BY CustomerName DESC;
# The following SQL statement shows the equivalent example for MySQL:
# e.g SELECT * FROM Customers ORDER BY CustomerName DESC LIMIT 3;
# The following SQL statement shows the equivalent example for Oracle:
# e.g SELECT * FROM Customers ORDER BY CustomerName DESC FETCH FIRST 3 ROWS ONLY;


"""
SQL Aggregate Functions
An aggregate function is a function that performs a calculation on a set of values, and returns a single value.

Aggregate functions are often used with the GROUP BY clause of the SELECT statement. The GROUP BY clause splits the result-set into groups of values and the aggregate function can be used to return a single value for each group.

The most commonly used SQL aggregate functions are:

MIN() - returns the smallest value within the selected column
MAX() - returns the largest value within the selected column
COUNT() - returns the number of rows in a set
SUM() - returns the total sum of a numerical column
AVG() - returns the average value of a numerical column
Aggregate functions ignore null values (except for COUNT(*)).
"""
# The MIN() function returns the smallest value of the selected column.
# The MAX() function returns the largest value of the selected column.
# e.g SELECT MIN(Price) FROM Products;
# e.g SELECT MAX(Price) FROM Products;
"""
SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MAX(column_name)
FROM table_name
WHERE condition;
"""
# When you use MIN() or MAX(), the returned column will not have a descriptive name.
# To give the column a descriptive name, use the AS keyword:
# e.g SELECT MIN(Price) AS SmallestPrice FROM Products;
# Here we use the MIN() function and the GROUP BY clause, to return the smallest price for each category in the Products table:
# e.g SELECT MIN(Price) AS SmallestPrice, CategoryID FROM Products GROUP BY CategoryID;

# The COUNT() function returns the number of rows that matches a specified criterion.
# e.g SELECT COUNT(*) FROM Products;
"""
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
"""
# NOTE: If you specify a column name instead of (*), NULL values will not be counted.
# Find the number of products where the ProductName is not null:
# e.g SELECT COUNT(ProductName) FROM Products;
# You can add a WHERE clause to specify conditions:
# e.g SELECT COUNT(ProductID) FROM Products WHERE Price > 20;
# You can ignore duplicates by using the DISTINCT keyword in the COUNT() function.
# If DISTINCT is specified, rows with the same value for the specified column will be counted as one.
# e.g SELECT COUNT(DISTINCT Price) FROM Products;
# Give the counted column a name by using the AS keyword.
# e.g SELECT COUNT(*) AS [Number of records] FROM Products;
# Here we use the COUNT() function and the GROUP BY clause, to return the number of records for each category in the Products table:
# e.g SELECT COUNT(*) AS [Number of records], CategoryID FROM Products GROUP BY CategoryID;

# The SUM() function returns the total sum of a numeric column.
# Return the sum of all Quantity fields in the OrderDetails table:
# e.g SELECT SUM(Quantity) FROM OrderDetails;
"""
SELECT SUM(column_name)
FROM table_name
WHERE condition;
"""
# SELECT SUM(Quantity) FROM OrderDetails WHERE ProductId = 11;
# Name the column "total":
# e.g SELECT SUM(Quantity) AS total FROM OrderDetails;
# Here we use the SUM() function and the GROUP BY clause, to return the Quantity for each OrderID in the OrderDetails table:
# e.g SELECT OrderID, SUM(Quantity) AS [Total Quantity] FROM OrderDetails GROUP BY OrderID;
# The parameter inside the SUM() function can also be an expression.
# If we assume that each product in the OrderDetails column costs 10 dollars, we can find the total earnings in
# dollars by multiply each quantity with 10:
# e.g SELECT SUM(Quantity * 10) FROM OrderDetails;
# We can also join the OrderDetails table to the Products table to find the actual amount, instead of assuming it is 10 dollars:
# Join OrderDetails with Products, and use SUM() to find the total amount:
# e.g SELECT SUM(Price * Quantity) FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;
