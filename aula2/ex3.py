# Ler dados do aluno
name = input("Digite o nome do aluno: ")
average = float(input("Digite a média do aluno: "))

student = {
    "name": name,
    "average": average
}

if average >= 5.0:
    student["status"] = "AP" 
else:
    student["status"] = "RP"

print("Dados do aluno:")
for key, value in student.items():
    print(f"{key}: {value}")
