import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'paises.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

region = np.char.strip(dataset[:, 1])
count = np.sum(region == 'NORTHERN AMERICA')
print(count)