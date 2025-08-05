number = int(input("Digite o número que deseja ver a tabuada: "))

start = int(input("Digite o início do intervalo: "))
end = int(input("Digite o fim do intervalo: "))

print(f"\nTabuada do {number} de {start} até {end}:\n")

for i in range(start, end + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
