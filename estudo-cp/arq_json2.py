import json
import os
os.system("cls")

# criando um dicionário aninhado
pessoas = {
    'pessoa1': {
        'nome' : 'edson',
        'idade': 48,
        'email': 'eds@hotmail.com'
    },

    'pessoa2': {
        'nome': 'jose',
        'idade': 23,
        'email': 'jose@fiap.com.br'
    },

    'pessoa 3' : {
        'nome': 'Maria',
        'idade': 44,
        'email': 'maria@fiap.com.br'
    },
}

pessoas_json = json.dumps(pessoas, indent = 4)
# exibindo o dicionário
print(pessoas)
# exibindo o objeto json
print()
print(pessoas_json)

# gravando no arquivo json
with open("arquivo.json", "w+") as file:
    # gravando o objeto no arquivo json
    file.write(pessoas_json)

with open("arquivo.json", "r") as file:
    # lendo o arquivo json
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

print(pessoas)
print()
print(pessoas_json)

# exibição formatada para o usuário
for k, v in pessoas.items():
    print(f"Registro...: {k}")
    for k1, v1, in v.items():
        print(f"\t{k1}: {v1}")

"""
EXERCÍCIO:
Criar um dicionário aninhado com 3 chaves no dicionário original

cria o menu:
0. sair
1. cadastrar
2. listar os registros
3. editar um registro

"""