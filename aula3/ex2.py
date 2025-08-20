import numpy as np

array_1 = np.array([i for i in range(0, 52, 2)])
print(array_1)

array_2 = np.array([i for i in range(100, 49, -2)])
print(array_2)

array_3 = np.sort(np.concatenate((array_1, array_2)))
print("Array ordenado: ", array_3)