import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, size=(4, 4))
print("Matriz 4x4 gerada:\n", matriz)

medias_linhas = matriz.mean(axis=1)
medias_colunas = matriz.mean(axis=0)

print("\nMédia de cada linha:", medias_linhas)
print("Média de cada coluna:", medias_colunas)

max_media_linhas = medias_linhas.max()
max_media_colunas = medias_colunas.max()

print("\nMaior média das linhas:", max_media_linhas)
print("Maior média das colunas:", max_media_colunas)

valores, contagens = np.unique(matriz, return_counts=True)

print("\nQuantidade de aparições de cada número:")
for v, c in zip(valores, contagens):
    print(f"Número {v} aparece {c} vez(es)")

numeros_2x = valores[contagens == 2]
print("\nNúmeros que aparecem 2 vezes:", numeros_2x)
