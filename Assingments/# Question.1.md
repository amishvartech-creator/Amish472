**create database**

create database Company_Management_db



**create table company**
(
companyid int primary key AUTO_INCREMENT,
companyname varchar(100),
street varchar(45),
city varchar(45),
state varchar(20),
zip varchar (10),   
)



**INSERT INTO Company** 

(CompanyName, Street, City, State, Zip)

VALUES 

('Vartech data Analytics', 'twins star building nana mauva', 'Rajkot', 'Gujrat', '360007'),
('Tretanz Infotech Solution', 'Bodakdev near pakwan restaurent', 'Ahemdabad', 'Gujrat', '380054'),
('Acme Corp', '123 Innovation way', 'Techcity', 'CA', '94016'),
('Stark Industries', '200 Park Ave', 'New YOrk', 'NY', '10166'),
('Wayne Enterprises', '1007 Mountain Drive', 'Gotham', 'NJ', '07001'),
('Cyberdyne Systems', '18111 Von Karman Ave', 'Irvine', 'CA', '92612');



**update company Name**

UPDATE Company
SET CompanyName = 'Coretus Reimageing Tech'
WHERE CompanyName = 'Acme Corp';