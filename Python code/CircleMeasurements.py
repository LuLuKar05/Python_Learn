import math
radius = float(input("Enter the radius of the circle: "))
area = round(math.pi * (radius ** 2), 2)
circumference = round(2 * math.pi * radius, 2)
print("The area of the circle is ",area,"and the circumference is ",circumference)