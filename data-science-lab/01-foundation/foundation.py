from numpy import average


print("Hello, Data Science !")

''''
Variable = box that store data
Data Types 
int = integer = whole number
float = decimal number
str = string = text
bool = boolean = True or False
'''

name ="Saruar"
age = 25
height = 5.9
is_student = True
print(f"My name is {name}. I am {age} years old. My height is {height} feet. Am I a student? {is_student}")

#Write a program that ask for 3 numbers, then prints:
#1. sum,average,max,min
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))
#without string to sum you have to use , between number for string +  

print(f"The sum is: {sum((number1,number2,number3))}")
print(f"The average is: {average((number1,number2,number3))}")
print(f"The maximum is : {max((number1,number2,number3))}")
print(f"The minimum is : {min((number1,number2,number3))}")
print("Hello, this is my first project")

'''
This is an f-string, a way to embed expressions inside string literals.

The expression inside {} is evaluated and inserted into the string.
'''