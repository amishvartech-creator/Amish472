**create table**

**create table Contact**
(
contactid int primary key AUTO_INCREMENT,
companyid int,
firstname varchar(45),
lastname varchar(45),
street varchar(45),
city varchar(45),
state varchar(20),
zip varchar (10), 
ismain boolean,
email varchar(45),
phone varchar(12) 
)

**INSERT INTO Contact**

(CompanyID, FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone)

VALUES 

(1, 'Moshe', 'Vardi', '5th Avenue#1001', 'New York', 'NY', '10036', TRUE, 'moshe@snjny.com', '212-921-4133'),
(2, 'John', 'Doe', '123 Main St', 'Los Angeles', 'CA', '90001', TRUE, 'john.doe@email.com', '215-555-0199'),
(3, 'Jane', 'Smith', '123 Main St', 'Los Angeles', 'CA', '90001', FALSE, 'jane.smith@email.com', '215-555-0122'),
(4, 'Dianne', 'Connor', '456 Oak Ave', 'New York', 'NY', '10001', TRUE, 'dianne.c@urbanout.com', '215-555-7744'),
(5, 'Mark', 'Johnson', '789 Pine Rd', 'Chicago', 'IL', '60601', TRUE, 'mjohnson@tollbros.com', '312-555-9876')







