camel = input("Please Enter something in the \"Lower Camel Case\": ")
snake =""

for i in camel:
    if i.isupper():
        snake += "_" + i.lower()
    else:
        snake += i
print("Your \"Snake Case\" is: ", snake)