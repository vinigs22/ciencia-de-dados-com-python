import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'paises.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

regions = dataset[:, 1] 
unique_regions = np.unique(regions, return_counts=True)

print(unique_regions, len(unique_regions))
