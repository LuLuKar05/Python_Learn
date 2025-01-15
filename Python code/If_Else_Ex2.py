threeDigitNumber = input("Enter 3-digits numbers:")
lengthOfNumber = len(threeDigitNumber)
leftMostNumber = threeDigitNumber[0]
try:
    threeDigitNumber = int(threeDigitNumber)
except:
    print("Please enter only number, thank you!!!(should be only numeric, no decimal allowed here)")
    quit
else: 
    if (lengthOfNumber != 3 ):
        print("Should be 3-digit number no bigger or less than 3")
        quit()
leftMostNumber = int(leftMostNumber)
if(leftMostNumber % 2 == 1):
    print("The number you entered starts with either 1, 3, 5, 7, or 9")
else:
    print("The left-most digit is an even digit.")
    print(leftMostNumber)