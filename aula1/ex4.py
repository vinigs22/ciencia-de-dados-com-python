distance = float(input("Qual é a distância da sua viagem? "))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

print(f"O preço da sua passagem será de R$ {price:.2f}")