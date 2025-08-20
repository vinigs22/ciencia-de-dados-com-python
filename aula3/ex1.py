import numpy as np

array_ones = np.ones(8)
array_random = np.random.randint(0, 10, 8)

array_sum = array_ones + array_random

if array_sum.sum() >= 40:
    array_sum = array_sum.reshape((4, 2))

print(array_sum)