time_str = input("Please Enter the time: ")
hours, minutes = map(int,time_str.split(":"))
time_float = hours + minutes / 60.0
print(time_float)
if time_float <= 8 and time_float >= 7:
    print("It's Breakfast-time")
elif time_float <= 13 and time_float >= 12:
    print("It's Lunch-time")
elif time_float <= 19 and time_float >= 18:
    print("It's Dinner_time")
else:
    print("take a nap!!!!")