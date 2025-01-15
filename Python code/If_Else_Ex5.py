threeDigitNumber = input("Enter 3-digits numbers:")
lengthOfNumber = len(threeDigitNumber)

try:
    threeDigitNumber = int(threeDigitNumber)
    
except:
    print("Wrong Input!!! Try Again.")
    quit
else: 
    if (lengthOfNumber != 3 ):
        print("Should be 3-digit number no bigger or less than 3")
        quit()
    firstNumber = int(threeDigitNumber[0])
    secondNumber = int(threeDigitNumber[1])
    thirdNumber = int(threeDigitNumber[2])
    sumOfAllDigits = firstNumber + secondNumber + thirdNumber
    if(sumOfAllDigits % 2 == 0):
        print("Sum of all digits is an even number")
    elif(sumOfAllDigits % 2 == 1):
        print("Sum of all digits is not an even number")

