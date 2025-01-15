# 48cookies=1.5cups_of_sugar+1cup_of_butter+2.75_cup_of_flour
# 48 = 1.5y + y + 2.75y
# 1 = 1.5(0.0208) + 0.0208 + 2.75(0.0208) 
# 1 = 0.0312 + 0.0208 + 0.0572

noOfCookies = int(input("Enter the amount of cookies you would like to:"))
#noOfCookies = int(noOfCookies)
cupsOfSugar = round(0.0312 * noOfCookies, 2)
cupsOfButter =round(0.0208 * noOfCookies, 2)
cupsOfFlour = round(0.0572 * noOfCookies, 2)
print("For", noOfCookies, ", you will need;\n" , cupsOfSugar, "cup of sugar \n", cupsOfButter ,"cup of Butter \n" ,cupsOfFlour," cup of Flour")

