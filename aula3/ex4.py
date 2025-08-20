import numpy as np

matriz = np.arange(12).reshape(3, 4)  
print("Matriz:")
print(matriz)

linhas, colunas = matriz.shape
print(f"\nLinhas: {linhas}, Colunas: {colunas}")

total = linhas * colunas
print(f"Total de elementos: {total}")

if total % 2 == 0:
    print("Essa matriz pode virar um vetor unidimensional com número PAR de elementos.")
else:
    print("Essa matriz pode virar um vetor unidimensional com número ÍMPAR de elementos.")
