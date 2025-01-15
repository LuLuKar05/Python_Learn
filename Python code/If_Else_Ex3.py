heroName = "Superman"
yourName = input("Enter your name, Please: ")
hero_power = len(heroName)
your_power = len(yourName)
if(your_power > hero_power):
    print("You are stronger than Superman.")
elif(your_power == hero_power):
    print("You are strong as Superman, be smart to beat him.")
else:
    print("You are weaker than an ant.")