n = int(input("Enter how many time:"))
total = 0 
negative_number = 0
positive_number = 0
for i in range(n):
    y = float(input(f"number#{i+1}"))
    if(y < 0):
        negative_number += y 
    else:
        positive_number += y
    total += y
average = total / n
print("The Average number is:", average)
print("The total positive number is:" ,positive_number)
print("The total negative number is:" ,negative_number)