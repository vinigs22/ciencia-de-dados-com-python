import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'social_media.csv')

dataset = np.loadtxt(file_path, delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

plataform = dataset[1:, 1]
region = dataset[1:, 4]
hashtag = dataset[1:, 2]
likes = dataset[1:, 5].astype(float)
views = dataset[1:, 6].astype(float)

# Questão 1 Quantidade de posts do Brasil
qtd_post_brazil = np.sum(region == 'Brazil')
print(qtd_post_brazil)

# Questão 2 Porcentagem de posts com a hashtag "Education
num_education = np.sum(hashtag == 'Education')
print( len(hashtag) / num_education)

# Questão 3 Colocar dentro de um dicionario e apresentar a média de likes e views dos posts do Instagram
dicionario = {}
dicionario['likes'] = likes[plataform == "Instagram"].mean()
dicionario['views'] = views[plataform == "Instagram"].mean()

print(dicionario['likes'])
print(dicionario['views'])

# Questão 4 Plataforma com maior número de posts
plataform_unique, counts = np.unique( plataform, return_counts=True)
index_max = counts.argmax()
print(plataform_unique[index_max])
print(counts[index_max])

# Questão 5 Região com maior número de likes
print(region[likes.argmax()])