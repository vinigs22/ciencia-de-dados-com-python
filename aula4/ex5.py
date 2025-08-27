import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

empresas_nome = dataset[:, 1]
empresas, counts = np.unique(empresas_nome, return_counts=True)
print("\nQuantidade de missões por empresa:")
for empresa, count in zip(empresas, counts):
    print(f"{empresa}: {count} missões")