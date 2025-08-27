import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

coluna_empresa = dataset[:, 1]
apenas_spacex = dataset[coluna_empresa == 'SpaceX']

coluna_custo_spacex = apenas_spacex[:, 6].astype(float)

indice_missao_mais_cara = np.argmax(coluna_custo_spacex)

print("Missão mais cara:", coluna_custo_spacex[indice_missao_mais_cara])
