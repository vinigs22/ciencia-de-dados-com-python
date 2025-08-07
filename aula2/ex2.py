store1_models = {"Iphone 12", "Iphone 15", "A30", "A50"}
store2_models = {"Iphone 12", "Iphone 15", "A50", "Motorola"}

print("Modelos vendidos pela Loja 1:", store1_models)
print("Modelos vendidos pela Loja 2:", store2_models)

all_models = store1_models | store2_models
print("Modelos disponíveis no total:", all_models)

models_in_both = store1_models & store2_models
print("Modelos disponíveis em ambas as lojas:", models_in_both)
