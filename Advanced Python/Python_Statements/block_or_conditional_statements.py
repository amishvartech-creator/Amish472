"""

 conditional statements :

  A conditional statements are used to check true or false 
  
  types of conditional statements 
  
    1. if 
    2. if else
    3. if elif
    4. nested if 
    5. switch (python not support)
  
  
  looping statements 
   
   A statements that can be iterate a values again and again there we used loop
   or
   A loop is repeated values again and again 
  
  types of loop 
   1. for 
   2. while 
     
"""

# conditional statements 

# if : if is executed when condition is true  
# syntax 
#  if condition:
#      statements

# examples
#a=2
#b=10
# if a>b:
#     print("a is greater than b")

# if a=b:
#     print("a is greater than b")

# if a>b:
#     print("a is greater than b")


# if else : if is executed when condition is true if condition is false else is executed  
# syntax 
#  if condition:
#      statements
#    else:
#        statements


# example
# a=15
# b=10
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is less than b")


# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is less than b")        


# nested if : if within another if i.e called nested if
#syntax
# if condition:
#     if condition:
#         statement
#     else:
#         statement


# a=10
# b=7
# if a>b:
#     if a!=0 and b!=0:
#      print("a is greater than b and both are positive numbers")
# else:
#       print("a is less than b")



# if elif : if is executed when condition is true elif is check multiple true conditions if conditions is false else is executed

# syntax 

# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# a=30
# b=30
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a and b both are same")        

# take input from users

# a=int(input("Enter a values :"))
# b=int(input("Enter b values :"))
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")    
# else:
#     print("a and b both are same")


# looping statements : 

# looping statements are executed number of iteration repeat again and again.
# loop is used to executed numbers of iteration again and again 

#syntax
# for i in range():
#     statement

# for i in range(1,10):
#     print(i)

# for i in range(1,100):
#     print(i)

            
# for i in range(1,100):
#     print(i,end=" ")

# for i in range(1,100):
#     print(i,end=" ,  ")


# loop with condition

# write a programme to print 1 to 10 and give only odd numbers

# for i in range(1,10):
#     if i%2==0:
#         print(i)

# for i in range(1,10):
#     if i%2==1:
#         print(i)


# employee=({"id":1,"name":"Amish","age":45,"department":"IT","address":"raiya road rajkot"})
# print(employee)
# print(type(employee))
# for i in employee:
#     print(employee["id"])
#     print(employee["name"])
#     print(employee["age"])
#     print(employee["department"])
#     print(employee["address"])


# employee=["Amish","Aryan","Dhairya","Om","Heer"]
# for i in employee:
#     print(i)


# employee={"fname":["Dhairya","Amish","Om","Heer"],"age":[14,45,13,12]}
# for i in employee["fname"]:
#     print(i)

# for i in employee["age"]:
#     print(i)


# while is a loop that can be executed when condition is true
# 
# # syntax 
# while condition:
#     statements
#     increments/decrements

# i=0
# while i<=10:
#     print(i)
#     i=i+1

# i=0
# while i<=10:
#     if i==5:
#         break
#     print(i)
#     i=i+1



# i=0
# while i<=10:
#     if i==5 or i==8:
#         i=i+1
#         continue
#     print(i)
#     i=i+1    


# i=0
# while i<=10:
#     if i  not in(5,8):
#         print(i)
#     i=i+1    



# i=0
# while i<=10:
#     print(i)
#     i=i+2