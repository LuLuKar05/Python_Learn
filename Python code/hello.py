def multiply(num: float):
  print(type(num))
  multiply = num * num
  return multiply
num_input = int(input("Enter number you would like to multiply"))
result = multiply(num_input)
print(f"{num_input} multiply by {num_input} is: {result}")