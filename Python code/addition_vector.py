import numpy as np
# Addition / Subtraction
vector_a = np.array([2, 4, 6])
vector_b = np.array([1, -2, 3])

addition = vector_a + vector_b
subtraction = vector_a - vector_b
print(addition)
print(subtraction)

# Scaling 
vector_a = np.array([3, 5 , -7])
multiply = 2 * vector_a
multiply_1 = -3 * vector_a
print(multiply, multiply_1)

#Dot Product 
vector_a = np.array([1, 3, 5])
vector_b = np.array([2, 4 ,6])
dot_product = np.dot(vector_a, vector_b)
print(dot_product)
# what a dot product of 0 means: my equation is it mean the two objects is completely identical