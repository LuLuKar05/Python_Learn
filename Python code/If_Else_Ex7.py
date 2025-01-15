electricUnit = input("Please Enter the used electric unit: ")
try:
    electricUnit = float(electricUnit)
except:
    print("Wrong input!!! try again")

else:
    electricUnit = round(electricUnit)
    electricUnit = electricUnit - 100
    if(electricUnit > 0):
        if(electricUnit <= 200):
            bill = electricUnit * 3
            print(f"Your total bill is {bill}")
        else:
            electricUnit = electricUnit - 200
            bill = 200 * 3 
            bill += electricUnit * 4
            print(f"Your total bill is {bill}")

    else:
        print("Your total bill is 0")