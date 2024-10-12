import os
os.system("cls")

usuarios = {}
print(usuarios)

# criando um registro - dicionario com uma lista dentro

usuarios = {
    'chave': ["Chaves do 8", "24/12/2017", "Recep_01"],
    'quico' : ["Quico das Flores", "20/12/2017", "RaioX_03"]
    }
print(usuarios)

# add valor
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)


# listar atribuições específicas de uma chave
print("-" * 20)
print(usuarios.get("quico"))