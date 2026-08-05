# What is  SQL and what is it used for ?

# SQL means

 **Structured Query Language**

 1. it is programmingg language to manage and manipulation of relational database.
 
 2. It is a declarative language used to create and modify database structures, insert, update, delete, and query data, and manage access and transactions.

 
 # What is the difference between 'Delete','Drop',and truncate ?

- **DELETE**:
  - Removes rows from a table.
  - You can use `WHERE` to delete specific rows.

- **DROP**:
  - Deletes the entire table or other database object.
  - It removes both the structure and the data.

- **TRUNCATE**:
  - Removes all rows from a table very quickly.


# Write a query to display all records from a table name 'Student' ?

```

SELECT * FROM Student;

```
 
 # Write a query to display only the name and age columns from the Student table ?

```

SELECT name, age FROM Student;

```

# how do you use the where clause ? gve an example

```

select * from student where id=1;

```


# write a query to display students whose age is greater than 18

```
select * from students where age > 18;

```


# What is the purpose of Order by clause ?


```

SELECT * FROM Students
ORDER BY age DESC;

```

# Write a Query to display students sorted by mark in desending order ?

```

select * from students order by marks desc 1,1;

```


# What is the difference between primary key and foreign key


**Primary Key**

1. pk is provides one time in table.

2. pk is in autoincremet primary key.

3. pk is never return null value in table.


**Foreign Key**

1. fk is provides more than once time in table

2. fk is provide relationaship b/w one table to another table with comman field or column name

3. fk is return duplicate values in table.


# Write a query to count the total  number of students ?

- select count(students) as total_number_students from students;


# Write a query to find the highest from an Employee table ?

- select max(salary) as highest_salary from employee;


# Write a query to calculate the average marks of students ?

- select avg(marks) as average_marks from students;


# Explain the use of like operator with example ?

1. Searching data from tables using keyword like operator is used

2. like operator is denoted by % symbol

- select * from employee where name like a%
- select * from employee where name like b%
- select * from employee where name like %a%
- select * from employee where name like a%h


# Write a Query to display students whose names start with A ?

- select * from students where name like a%;


# What is the purpose of Join clause ?

- SQL join are used to more than one tables with common fields or column name.


# Explain the difference between Inner Join and Left Join ?

**Inner Join**

1. SQL Inner Join are used to more than one tables with common fields.

2. If Data is matched from first table to second table with common field its join otherwise return null values.


**left join**

1. SQL  left join are used to join 1st table of left rows to 2nd table of left rows if data is matched join all otherwise return null values. 


# Write a query to display employee names along with their department names using joins ?

- select employee.*,depname from employee join department on employee.departmentid=department.departmentid;


# Write a query to find the secone highest salary from an Employee table ?


- select max(salary) as second_highest_salary from employee where salary < (select max(salary) from employee);


- select * from employee order by employee_salary desc limit 1,1;




