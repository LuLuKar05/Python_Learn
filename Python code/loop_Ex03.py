number = int (input("Please enter the value: "))
total = number
if number <= 0:
    print("Number can't be negative or Zero")
    quit
while number > 1:
    number -= 1
    print(number)
    total += number
print(total)
# print number => into list , and can used later all the number and used for later.
