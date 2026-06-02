**create table**

**create table ContactEmployee**
(
contactemployeeid int primary key AUTO_INCREMENT,
contactid int,
employeeid int,
contactdate varchar(45),
description varchar(100) 
)


**INSERT INTO ContactEmployee**

(ContactID, EmployeeID, ContactDate, Description)

VALUES 

(3, 1, '2024-05-10', 'Jack Lee met Dianne Connor from Coretus Reimaging Tech to discuss the new Q3 marketing strategy.'),
(1, 1, '2024-05-12', 'Follow-up call with John Doe regarding contract renewal terms.'),
(4, 2, '2024-05-14', 'Lesley Bland introduction call with Mark Johnson from Toll Brothers.'),
(2, 3, '2024-05-15', 'Sarah Conner provided technical support documentation to Jane Smith.');
