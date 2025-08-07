peoples = []

for i in range(3):
    name = input(f"Digite o nome da pessoa {i+1}: ")
    weight = float(input(f"Digite o peso da pessoa {i+1}: "))

    person = {
        "name": name,
        "weight": weight
    }
    peoples.append(person)

heaviest_person = max(peoples, key=lambda p: p["weight"])
lightest_person = min(peoples, key=lambda p: p["weight"])

print(f"A pessoa mais pesada é {heaviest_person['name']} com {heaviest_person['weight']} kg.")
print(f"A pessoa mais leve é {lightest_person['name']} com {lightest_person['weight']} kg.")
