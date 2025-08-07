people = []

n = int(input("Digite a quantidade de pessoas: "))

for i in range(n):
    name = input(f"Digite o nome da pessoa {i+1}: ")
    age = int(input("Digite a idade da pessoa: "))
    gender = input("Digite o sexo da pessoa (M/F): ").strip().upper()

    person = {
        "name": name,
        "age": age,
        "gender": gender
    }
    people.append(person)

total_age = sum(person["age"] for person in people)
average_age = total_age / n

print(f"\nA média de idades é: {average_age:.2f}")

young_women = [p for p in people if p["gender"] == "F" and p["age"] < 20]
print(f"Quantidade de mulheres com menos de 20 anos: {len(young_women)}")
