#The program is already given all the value. so it would be better to used constant value in this one.
no_shares = 2000
buy_share_rate = 40.00
amount_of_buy = no_shares * buy_share_rate
sell_share_rate = 42.75 
amount_of_sell = no_shares * sell_share_rate
paid_stockbroker_buy = (amount_of_buy) * 0.03
paid_stockbroker_sell = (amount_of_sell) * 0.03
profit = (amount_of_sell - amount_of_buy) - (paid_stockbroker_buy + paid_stockbroker_sell)
print("The amount of money paid for the stock: ",amount_of_buy,"$\nThe amount of commission to his broker when he bought the stock: ",paid_stockbroker_buy,"$ \nThe amount for stock when sold: ",amount_of_sell,"$ \nThe amount of commission paid when he sell the stock ",paid_stockbroker_sell,"$\n ")
print("The profit he make is:",profit)
if(profit < 0):
    print("He is making losses.")

else:
    print("He is making profit.")
