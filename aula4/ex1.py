import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

status_coluna = dataset[:, 7]  

total_missoes = len(status_coluna)
print("Total de missões:", total_missoes)

total_missoes_sucesso = np.count_nonzero(status_coluna == 'Success')
print("Total de missões com sucesso:", total_missoes_sucesso/total_missoes*100, "%")