start = int(input("Please enter the starting column of number of each row."))
end = int(input("Please enter the ending column number of each row."))
step = int(input ("Please enter the number of vacant seats between two persons in each row."))
a = 0
print("the following column number will be available:")
for i in range(start,end,step + 1):
    print(i)
    a += 1
a = a * 10
print(f"there is a total of {a} available seat.")