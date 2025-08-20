import numpy as np
import random

matriz = np.zeros((2, 2), dtype=int)

linha = random.randint(0, 1)
coluna = random.randint(0, 1)
matriz[linha, coluna] = 1

tentativas = 0
acertou = False

while tentativas < 3:
    print("\nJogada", tentativas + 1)
    x = int(input("Escolha a linha (0 ou 1): "))
    y = int(input("Escolha a coluna (0 ou 1): "))

    if matriz[x, y] == 1:  
        print("Game Over! :( Try Again!")
        acertou = True
        break
    else:
        print("Posição segura! Continue jogando...")
    tentativas += 1

if not acertou:
    print("Congratulations! You beat the game! :)")
