while True:
    gender = input("Digite seu sexo (M para masculino / F para feminino): ").strip().upper()
    
    if gender == "M":
        print("Você é homem.")
        break
    elif gender == "F":
        print("Você é mulher.")
        break
    else:
        print("Entrada inválida. Por favor, digite M ou F.")