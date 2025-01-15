firstint = int(input("Please enter the first integer"))
secondint = int(input("Please enter the second integer"))
values = []
if firstint > secondint:
    b = firstint
    s = secondint
elif secondint > firstint:
    b = secondint
    s = firstint
else:
    print("Enter different Value, please. This one is same values for the 2 variables")

while b >= s:
    values.append(b)
    b -= 1
print(values)