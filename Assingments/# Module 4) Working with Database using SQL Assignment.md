# For this assignment, you will finish building the contact management database for MarketCo

**Answer**


# create database

**create database Contact_management_marketco**



1) # Statement to create the Company


**create table company** 

   ````

(
 companyid int primary key AUTO_INCREMENT, 
 companyname varchar(100),
 street varchar(45), 
 city varchar(45), 
 state varchar(20), 
 zip varchar (10),
)


````


**INSERT INTO Company**

````

(CompanyName, Street, City, State, Zip)

VALUES

('Vartech data Analytics', 'twins star building nana mauva', 'Rajkot', 'Gujrat', '360007'), ('Tretanz Infotech Solution', 'Bodakdev near pakwan restaurent', 'Ahemdabad', 'Gujrat', '380054'),
('Acme Corp', '123 Innovation way', 'Techcity', 'CA', '94016'), ('Stark Industries', '200 Park Ave', 'New YOrk', 'NY', '10166'), 
('Wayne Enterprises', '1007 Mountain Drive', 'Gotham', 'NJ', '07001'), 
('Cyberdyne Systems', '18111 Von Karman Ave', 'Irvine', 'CA', '92612');

````


2) # Statement to create the Contact table

# create table Contact

````

create table Contact 

( 
contactid int primary key AUTO_INCREMENT, companyid int, 
Firstname varchar(45), 
Lastname varchar(45), 
Street varchar(45), 
City varchar(45), 
State varchar(20), 
Zip varchar (10), 
IsMain boolean, 
Email varchar(45), 
Phone varchar(12) 
)

````

# INSERT INTO Contact

````
(Companyid,FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone)

VALUES

(1, 'Moshe', 'Vardi', '5th Avenue#1001', 'New York', 'NY', '10036', TRUE, 'moshe@snjny.com', '212-921-4133'),

(2, 'John', 'Doe', '123 Main St', 'Los Angeles', 'CA', '90001', TRUE, 'john.doe@email.com', '215-555-0199'), 

(3, 'Jane', 'Smith', '123 Main St', 'Los Angeles', 'CA', '90001', FALSE, 'jane.smith@email.com', '215-555-0122'),

(4, 'Dianne', 'Connor', '456 Oak Ave', 'New York', 'NY', '10001', TRUE, 'dianne.c@urbanout.com', '215-555-7744'),

(5, 'Mark', 'Johnson', '789 Pine Rd', 'Chicago', 'IL', '60601', TRUE, 'mjohnson@tollbros.com', '312-555-9876')

````


3) # Statement to create the Employee table 


# create table employee

````
create table Employee

( 
Employeeid int primary key AUTO_INCREMENT, 
Firstname varchar(45),
Lastname varchar(45), 
Salary float, 
Hiredate varchar(45), 
Jobtitle varchar(25), 
Email varchar(45), 
Phone varchar(20) 
 )

````

**INSERT INTO Employee**

````
(employeeid,FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone)

VALUES

('Jack', 'Lee', 75000.00, '2021-03-15', 'Account Manager', 'jack.lee@marketco.com', '215-555-0144'), 
('Lesley', 'Bland', 68000.00, '2022-06-01', 'Sales Representative', 'lesley.b@marketco.com', '215-555-3322'), 
('Sarah', 'Conner', 95000.00, '2019-11-12', 'Director of Sales', 's.conner@marketco.com', '215-555-9988'), 
('Michael', 'Green', 52000.00, '2023-01-15', 'Support Specialist', 'm.green@marketco.com', '215-555-4455'),
('Moshe', 'Vardi', 45000.00, '2015-03-15', 'Sales Representative', 'moshe@snjny.com', '212-921-4133'),
('Sharon', 'Praude', 100000.00, '2010-03-15', 'Manager', 'sharon@gmail.com', '215-444-3322'),('Sarah', 'Khan', 35000.00, '2024-03-15', 'sales', 's.khan@marketco.com', '215-231-9988'),('Priyank', 'Sepany', 22000.00, '2025-03-15', 'Support Specialist', 'p.sepany@marketco.com', '215-333-3314');

````


4) # Statement to create the ContactEmployee table

HINT: Use DATE as the datatype for ContactDate. It allows you to store the
date in this format: YYYY-MM-DD (i.e., ‘2014-03-12’ for March 12, 2014). 



# create table ContactEmployee

````

create table ContactEmployee 

( 
contactemployeeid int primary key AUTO_INCREMENT,
contactid int references contact(Contactid),
employeeid int references employee(Employeeid), 
contactdate varchar(45), 
description varchar(100) 
)

 ````



**INSERT INTO ContactEmployee**

````

(ContactID, EmployeeID, ContactDate, Description)

VALUES

(3, 1, '2024-05-10', 'Jack Lee met Dianne Connor from Coretus Reimaging Tech to discuss the new Q3 marketing strategy.'),
(1, 1, '2024-05-12', 'Follow-up call with John Doe regarding contract renewal terms.'),
(4, 2, '2024-05-14', 'Lesley Bland introduction call with Mark Johnson from Toll Brothers.'), 
(2, 3, '2024-05-15', 'Sarah Conner provided technical support documentation to Jane Smith.');


````


5) # In the Employee table, the statement that changes Lesley Bland’s phone number to 215-555-8800
      

**Update phone number in emplooyee table**

````

UPDATE emplooyee SET Phone = '215-555-8800' WHERE firstName = 'Lesley' AND lastName = 'Bland';

````



6) # In the Company table, the statement that changes the name of “Acme Corp” to “Cortus Reimaging Technology” 


**update company Name**

````

UPDATE Company SET CompanyName = 'Coretus Reimageing Technology' WHERE CompanyName = 'Acme Corp';

````




7) # In ContactEmployee table, the statement that removes Dianne Connor’s contact

    event with Jack Lee (one statement).
    HINT: Use the primary key of the ContactEmployee table to specify the correct record to remove.

    ````

    DELETE FROM ContactEmployee WHERE ContactID = 4 AND EmployeeID = 1;
    

    ````






8) # Write the SQL SELECT query that displays the names of the employees that

    have contacted Toll Brothers (one statement). Run the SQL SELECT query in
    MySQL Workbench. Copy the results below as well







9) # What is the significance of “%” and “_” operators in the LIKE statement? 









10) # Explain normalization in the context of databases.














11) # What does a join in MySQL mean?













12) # 19.What do you understand about DDL, DCL, and DML in MySQL?

````

1. DDL (Data Definition Language)


DDL commands are used to define, alter, or modify the structure (schema) of your database objects, such as tables, databases, views, and indexes.

Key Characteristic: DDL operations deal with the blueprint of the database, not the actual data rows. In MySQL, DDL statements are auto-committed, meaning changes are saved instantly and cannot be rolled back.

Common Commands:

CREATE: Creates a new database or table (e.g., CREATE TABLE Employees (...);).

ALTER: Modifies an existing database structure (e.g., adding a new column).

DROP: Deletes an entire table or database structure along with all its data.

TRUNCATE: Removes all records from a table, resetting it completely while keeping the empty structure intact.

````


````

2. DML (Data Manipulation Language)

DML commands are used to manage and manipulate the data residing inside the existing database objects. Once DDL creates the tables, DML is what you use to populate and change the records.

Key Characteristic: Unlike DDL, DML operations can be managed using transactions (COMMIT and ROLLBACK), allowing you to undo changes before they are finalized.

Common Commands:

INSERT: Adds new rows of data into a table (e.g., INSERT INTO Employees VALUES (...);).

UPDATE: Modifies existing data within a table.

DELETE: Removes specific rows from a table based on a condition (unlike TRUNCATE, you can delete just one row).

(Note: SELECT is sometimes categorized under DML, though it is officially part of DQL—Data Query Language—since it only retrieves data without manipulating it).

````



````

3. DCL (Data Control Language)

DCL commands are used to enforce database security by managing user permissions and access rights. They control who can view or modify the data and structures.

Key Characteristic: DCL is strictly administrative. It ensures that only authorized database administrators (DBAs) or specific users can execute DDL or DML commands.

Common Commands:

GRANT: Gives a user permission to perform specific tasks (e.g., granting a user permission to SELECT from a table).

REVOKE: Takes away previously granted permissions from a user.


````




13) # What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?



       























