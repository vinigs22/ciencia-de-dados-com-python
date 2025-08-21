import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

coluna_custo = dataset[:, 6].astype(float)

valores_validos = coluna_custo[coluna_custo > 0]

numero_total = len(valores_validos)
print("Número total de valores disponíveis:", numero_total)

custo_total = np.sum(valores_validos)
print("Custo total:", custo_total)

custo_medio = np.mean(valores_validos)
print("Custo médio:", custo_medio)
