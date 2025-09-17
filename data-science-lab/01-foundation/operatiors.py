'''
Operatiors in Python
Arithmetic Operators + - * / % // **
Comparison Operators == != > < >= <=
** power
% remainder
'''

''''''
num1=int(input("Enter the number"))
num2=int(input("Enter the number :"))

print(num1,num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)


#Hard 
#BMI Calculator
#Input weight & height
#Formula: bmi = weight/ (height*height)

weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in cm:"))
bmi = weight / (height / 100) ** 2
print(f"Your BMI is: {bmi}")
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<24.9 :
    print("Normal")
elif 25<=bmi<30.2 :
    print("Overweight")