**create table**

**create table Employee**
(
employeeid int primary key AUTO_INCREMENT,
firstname varchar(45),
lastname varchar(45),
salary float,
hiredate varchar(45),
jobtitle varchar(25),
email varchar(45),
phone varchar(20) 
)


**INSERT INTO Employee**

(employeeid,FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone)

VALUES 

('Jack', 'Lee', 75000.00, '2021-03-15', 'Account Manager', 'jack.lee@marketco.com', '215-555-0144'),
('Lesley', 'Bland', 68000.00, '2022-06-01', 'Sales Representative', 'lesley.b@marketco.com', '215-555-3322'),
('Sarah', 'Conner', 95000.00, '2019-11-12', 'Director of Sales', 's.conner@marketco.com', '215-555-9988'),
('Michael', 'Green', 52000.00, '2023-01-15', 'Support Specialist', 'm.green@marketco.com', '215-555-4455'),('Moshe', 'Vardi', 45000.00, '2015-03-15', 'Sales Representative', 'moshe@snjny.com', '212-921-4133'),('Sharon', 'Praude', 100000.00, '2010-03-15', 'Manager', 'sharon@gmail.com', '215-444-3322'),('Sarah', 'Khan', 35000.00, '2024-03-15', 'sales', 's.khan@marketco.com', '215-231-9988'),('Priyank', 'Sepany', 22000.00, '2025-03-15', 'Support Specialist', 'p.sepany@marketco.com', '215-333-3314');


**Update phone number in emplooyee table**

UPDATE emplooyee
SET Phone = '215-555-8800'
WHERE firstName = 'Lesley' AND lastName = 'Bland';