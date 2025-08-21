import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

coluna_empresa = dataset[:, 1]
total_count = np.sum((coluna_empresa == 'NASA') | (coluna_empresa == 'SpaceX'))

print("Total NASA e SpaceX:", total_count)


