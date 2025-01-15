male = float(input("Enter the number of males in the class room:"))
female = float(input("Enter the number of female in the class room: "))
total_student = male + female
percentage_Of_Male = round(male / total_student * 100, 2)
percentage_Of_Female = round(female / total_student * 100, 2) #100 - percentage_Of_Male
print("The percentage of male in the classroom is: ",percentage_Of_Male,"% \nThe percentage of Female in the classroom is: ", percentage_Of_Female, "%")