# For this assignment, you will finish building the contact management database for MarketCo

#  How to create database

**syntax ....**


create database contact_management_marketco


1) # Statement to create the Company



**syntax to create table** 

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


**SQL Query:**

````sql
SELECT DISTINCT e.FirstName, e.LastName
FROM Employee e
INNER JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
INNER JOIN Contact c ON ce.ContactID = c.ContactID
INNER JOIN Company co ON c.CompanyID = co.CompanyID
WHERE co.CompanyName = 'Toll Brothers';
````

**Query Results:**

| FirstName | LastName |
|-----------|----------|
| Lesley    | Bland    |







9) # What is the significance of “%” and “_” operators in the LIKE statement? 


The "%" and "_" are **wildcard operators** used in the LIKE statement to match patterns in string data:

**"%" (Percent Sign) - Matches Zero or More Characters**
- Represents any number of characters (including zero)
- Used to search for a pattern anywhere in the string
- Examples:
  - `WHERE FirstName LIKE 'J%'` → Matches "Jack", "John", "Jane", "Jessica"
  - `WHERE Email LIKE '%@marketco.com'` → Matches any email ending with "@marketco.com"
  - `WHERE City LIKE '%York%'` → Matches "New York", "York", "New York City"

**"_" (Underscore) - Matches Exactly One Character**
- Represents exactly one single character
- Used when you know a string has a specific length or pattern
- Examples:
  - `WHERE Phone LIKE '215-555-____'` → Matches any phone starting with "215-555-" followed by exactly 4 digits
  - `WHERE State LIKE '__'` → Matches any two-letter state code like "NY", "CA", "NJ"
  - `WHERE LastName LIKE '_mith'` → Matches "Smith", "Amith" but NOT "Smith" (needs exactly one character before "mith")

**Key Differences:**
| Operator | Matches | Example |
|----------|---------|---------|
| % | 0 or more characters | `'S%'` matches "Sarah", "Sharon", "S" |
| _ | Exactly 1 character | `'S_'` matches only 2-character strings starting with "S" |

**Practical SQL Examples from Your Database:**
- `SELECT * FROM Contact WHERE FirstName LIKE 'J%'` → Finds all contacts starting with "J"
- `SELECT * FROM Employee WHERE Phone LIKE '215-555-____'` → Finds all employees with specific phone pattern
- `SELECT * FROM Company WHERE CompanyName LIKE '%Tech%'` → Finds companies with "Tech" in their name






10) # Explain normalization in the context of databases.


**Database Normalization** is a systematic process of organizing data in a database to reduce redundancy, eliminate data anomalies, and improve data integrity. It involves decomposing tables into smaller, well-structured tables and defining relationships between them.

## Why Normalize a Database?

- **Eliminates Data Redundancy:** Avoids storing the same data in multiple places
- **Prevents Data Anomalies:** Reduces insertion, update, and deletion errors
- **Improves Data Integrity:** Ensures accurate and consistent data
- **Optimizes Storage:** Reduces disk space usage
- **Simplifies Maintenance:** Makes updates and modifications easier
- **Enhances Query Performance:** Properly indexed normalized databases query faster

## Normal Forms (Levels of Normalization)

### **1st Normal Form (1NF)**
- All attributes must contain atomic (indivisible) values
- Each column should contain only single values, not lists or arrays
- Remove repeating groups into separate tables
- Example: Instead of storing multiple phone numbers in one field, create a separate Phones table

### **2nd Normal Form (2NF)**
- Must meet 1NF requirements
- Remove partial dependencies: Non-key attributes must depend on the ENTIRE primary key
- All non-key columns should be fully dependent on the primary key
- Example: In your Employee table, Salary depends entirely on EmployeeID (not on part of a composite key)

### **3rd Normal Form (3NF)**
- Must meet 2NF requirements
- Remove transitive dependencies: Non-key attributes should not depend on other non-key attributes
- No column should depend on another column that isn't the primary key
- Example: In Contact table, City and State should not be stored together with employee data if they could change independently

### **Higher Normal Forms (4NF, 5NF, BCNF)**
- **Boyce-Codd Normal Form (BCNF):** Stricter version of 3NF
- **4th Normal Form (4NF):** Handles multivalued dependencies
- **5th Normal Form (5NF):** Handles join dependencies
- Most practical applications stop at 3NF

## Example from Your MarketCo Database

**Before Normalization (Redundant Data):**
```
Contact_Company Table:
ContactID | FirstName | LastName | CompanyID | CompanyName | Street | City | State | Zip | Email
1         | Moshe     | Vardi    | 1         | Vartech     | 5th Ave| NY   | NY   | 10036 | moshe@snjny.com
2         | John      | Doe      | 1         | Vartech     | 5th Ave| NY   | NY   | 10036 | john.doe@email.com
(Notice: Company info repeated for every contact)
```

**After Normalization (3NF):**
```
Company Table:
CompanyID | CompanyName | Street | City | State | Zip

Contact Table:
ContactID | FirstName | LastName | CompanyID | Email
(CompanyID references Company table)

ContactEmployee Table:
ContactEmployeeID | ContactID | EmployeeID | ContactDate | Description
```

**Benefits in Your Design:**
- Company information is stored once in the Company table
- If "Vartech" changes its address, you update it in ONE place
- Contacts link to companies via foreign key, eliminating redundancy
- The ContactEmployee table tracks interactions without duplicating employee or contact data



11) # What does a join in MySQL mean?


A **JOIN** in MySQL is a SQL operation that combines rows from two or more tables based on a related column shared between them. It allows you to retrieve related data stored in separate tables as a single result set.

**Why joins are used:**

- Connect related records across tables
- Keep data normalized by avoiding repeated information
- Retrieve combined data without duplicating it in one table


**Common join types:**

- `INNER JOIN`: returns only rows that match in both tables

- `LEFT JOIN` / `LEFT OUTER JOIN`: returns all rows from the left table and matching rows from the right table; non-matching right-side rows return `NULL`

- `RIGHT JOIN` / `RIGHT OUTER JOIN`: returns all rows from the right table and matching rows from the left table; non-matching left-side rows return `NULL`

- `FULL JOIN` / `FULL OUTER JOIN`: returns rows when there is a match in either table (MySQL does not support it directly without a workaround)

- `CROSS JOIN`: returns the Cartesian product of both tables


**Example in your MarketCo database:**

```sql
SELECT e.FirstName, e.LastName, c.FirstName AS ContactFirstName, c.LastName AS ContactLastName
FROM Employee e
INNER JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
INNER JOIN Contact c ON ce.ContactID = c.ContactID;
```

This query joins employees with the contacts they have interacted with, combining data from `Employee`, `ContactEmployee`, and `Contact`.







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


A **JOIN** clause in MySQL is used to combine rows from two or more tables based on a related column. Its role is to let you query linked data across tables so that you can work with related information without duplicating it in a single table.

**Role of the JOIN clause:**
- Connects data stored in separate tables using keys or matching columns
- Enables retrieval of combined row sets from multiple tables
- Supports normalized database design by keeping data in its proper table and linking it when needed
- Helps answer complex questions that depend on multiple entities, such as employees and contacts, companies and addresses, or transactions and customers

**Common types of joins in MySQL:**
- `INNER JOIN`: returns only rows that have matching values in both tables
- `LEFT JOIN` / `LEFT OUTER JOIN`: returns all rows from the left table, and matching rows from the right table; non-matching right-side rows return `NULL`
- `RIGHT JOIN` / `RIGHT OUTER JOIN`: returns all rows from the right table, and matching rows from the left table; non-matching left-side rows return `NULL`
- `FULL JOIN` / `FULL OUTER JOIN`: returns rows when there is a match in either table (MySQL does not support this directly without a workaround)
- `CROSS JOIN`: returns every combination of rows from both tables (Cartesian product)

**Example:**
```sql
SELECT e.FirstName, e.LastName, c.CompanyName
FROM Employee e
INNER JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
INNER JOIN Contact c ON ce.ContactID = c.ContactID;
```
This example uses JOINs to combine employee data with contact events and contact details in one result.


       























