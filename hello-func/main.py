import numpy as np

print("\nHere's a Numpy Example")
arr = np.array([1, 2, 3, 4, 5, 4, 4, 5, 4])

x = np.where(arr == 4)

print(x)