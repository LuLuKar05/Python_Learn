username = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Next Year, your age will be {age +1},{username}")
##alternative solution
import datetime #import the method to used the date that currently we are 
username = input("Enter your name: ")
DOB = input("Enter your Date of Birth: ")
current_datetime = datetime.now()
current_year = datetime.datetime.now().year
age = current_year - DOB 
print(f"Welcome {username} and your age is {age}")
## Double the number 
number = float(input("Enter your number:"))
multiplier = number * 2
## Double the number // alternative solution (more dynamic one)
number = float(input("Enter your number:"))
multiplier = float(input("Enter the number, that you want to multiply"))
print(f"your answer is:{multiplier}") 


#Activity1
print("Myo Myat Thiha")
#Activity2 
sum = 1 +4
print(f"the total is{sum}")
#Activity3
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"your name is {name} and {age} year old")
#Activity4
num1 = float(input("Enter your first number"))
num2 = float(input("Enter your second number"))
operactor =int(input('''Enter 1 for sum,
                    Enter 2 for  Subtracts, 
                     Enter 3 for multiplies or
                     Enter 4 for divides '''))
if operactor ==1:
    print(num1 + num2)
elif operactor ==2:
    print(num1-num2)
elif operactor == 3:
    print(num1 * num2)
elif operactor == 4:
    print(num1 / num2)
else:
    print("Enter only 1-4 please")