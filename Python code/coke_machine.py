coke = 50 
numberOfCoke = int(input("Enter how many coke you want: "))
coins = [25, 10 , 5]
chargesOfCoke = coke * numberOfCoke
while chargesOfCoke > 0:
    print("Total is: ", chargesOfCoke)
    userInsertMoney = int(input("Please Enter your coins and it should be only 25, 10 and 5: "))
    if userInsertMoney in coins:
        chargesOfCoke -= userInsertMoney
        print(f"You have to pay {chargesOfCoke} more.")
    else:
        print("Please Enter only 25, 10 or 5 coins, Please...")
        quit
chargesOfCoke = str(chargesOfCoke)
if not chargesOfCoke.isdigit():
    b = chargesOfCoke[1::]
    print("Here is your changes: ", b) 
###  Chat-GPT code ###
# coke = 50
# accepted_coin = [25, 10, 5]
# total_inserted = 0 
# print("Coke Machine: The price of a coke is 50 cents.")
# no_of_coke = int(input(" Enter how many coke you want: "))
# total_have_to_pay = coke * no_of_coke
# print(f'''The Total is {total_have_to_pay}$ for the {no_of_coke} cokes,
#        Please insert coins (Accepted coins: 25, 10, 5).''')
# Loop until the total inserted money is enough to pay for the coke
# while total_inserted < total_have_to_pay:
#     try:
#         coin = int(input(f"Insert a coin (Remaining: {total_have_to_pay - total_inserted}): ")) #Shown the remaining when it asked to insert make more efficient
#         if coin in accepted_coins: # checked the input coin is at the list, if not accept.
#                 total_inserted += coin
#         else:
#                 print(f"Invalid coin! Only {accepted_coins} are accepted.")
#     except ValueError:
#             print("Invalid input. Please insert a valid coin.")

    # Calculate change to give back, if any
# change = total_inserted - total_have_to_pay

# if change > 0:
#         print(f"Thank you! Dispensing coke and returning {change} cents as change.")
# else:
#         print("Thank you! Dispensing coke.")