import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'space.csv')

# Carregar CSV como string, pulando cabeçalho
dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

# Selecionar apenas missões da SpaceX
coluna_empresa = dataset[:, 1]
apenas_spacex = dataset[coluna_empresa == 'SpaceX']

# Selecionar coluna de custos (H → índice 7) e converter para float
coluna_custo_spacex = apenas_spacex[:, 6].astype(float)

# Índice da missão mais cara
indice_missao_mais_cara = np.argmax(coluna_custo_spacex)

print("Missão mais cara:", coluna_custo_spacex[indice_missao_mais_cara])
