full_name = input("Digite seu nome completo: ").strip()

print("\nNome em letras maiúsculas:", full_name.upper())

print("Nome em letras minúsculas:", full_name.lower())

number_of_letters = len(full_name.replace(" ", ""))
print("Total de letras no nome:", number_of_letters)

split_name = full_name.split()
if len(split_name) > 1:
    split_name[-1] = "do Inatel"
    new_name = " ".join(split_name)
else:
    new_name = full_name + " do Inatel"

print("Nome com último sobrenome trocado por 'do Inatel':", new_name)
