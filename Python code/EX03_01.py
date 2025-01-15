work_Hour = float(input("Enter your work hour: "))
pay_Rate = float(input("Enter your pay rate: "))
pay_Check = work_Hour * pay_Rate

if(work_Hour > 40):
    org_Fee = 40 * pay_Rate
    over_Time = work_Hour - 40 
    over_Time_Pay_Rate = pay_Rate * 1.5
    over_Time_Fee = over_Time * over_Time_Pay_Rate
    print("You are working", over_Time,"hr over-time and your over-time fee is ",over_Time_Fee,)
    print("Your total payment is: ",org_Fee + over_Time_Fee,)
else:
    print("You are working regular, your working hr is:",work_Hour, "and the total payment is:", pay_Check)
