# V is the number of grapevines that will fit in the row.
#R is the length of the row, in feet
#E is the amount of space, in feet
#S id the space between vines 

R= float(input("Enter the length of the row: "))
E = float(input("Enter the amount of space:" )) 
S = float(input("Enter the space between vines: "))

V = round((R - 2 * E) / S, 2)
print("The number of grapevines that will fit in the row is:" ,V)
