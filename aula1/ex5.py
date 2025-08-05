number = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= number <= 9999:
    unit = number % 10
    ten = (number // 10) % 10
    hundred = (number // 100) % 10
    thousand = number // 1000

    print(f"Unidade: {unit}")
    print(f"Dezena: {ten}")
    print(f"Centena: {hundred}")
    print(f"Milhar: {thousand}")
else:
    print("Número inválido. Digite um valor entre 1000 e 9999.")