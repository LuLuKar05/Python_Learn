numX = int(input("Enter your First Number: "))
numY = int(input("Enter your Second Number: "))
numZ = int(input("Enter your Third Number: "))
if (numX > numY):
    if(numY > numZ):
        print("Your middle value is",numY)
    elif(numZ > numY):
        print("Your middle value is ",numZ)
elif(numY > numX):
    if(numX > numZ):
        print("Your middle value is ",numX)
    elif(numZ > numX):
        print("Your middle value is", numZ)
elif(numZ > numY):
    if(numY > numX):
        print("Your middle value is",numY)
    elif(numX > numY):
        print("Your middle value is ",numX)

