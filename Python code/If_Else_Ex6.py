height = float(input("Enter your height in cm ,please: "))
if (height < 80):
    print(f"Your height is {height}cm. and you are too short for this ride.")
elif( height >= 80 and height <= 180 ):
    print("Your height is ok for this ride")
else:
    print(f"Your height is {height} and it\'s too tall for this ride")
