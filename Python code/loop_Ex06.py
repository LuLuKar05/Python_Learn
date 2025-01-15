integer = input("Please enter the number: ")  # accept as string
total_sum = 0

for i in integer:  #will loop every char in the integer// that while remain as string
    i = int(i) #change onlt the chr to int 
    if i % 2 == 0:  # Check if the number is even
        total_sum += i  # Add the even number to the sum

print(f"The sum of Even digit is: {total_sum}")