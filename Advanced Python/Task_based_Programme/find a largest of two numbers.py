# largest of two numbers using loop

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

numbers = [num1, num2]
largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num

print("The largest number is:", largest)
