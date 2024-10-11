import json
import os
os.system("cls")

# criando um dicionário
contato = {
    'nome': 'edson',
    'idade': 50,
    'cel': '11948376362'
}

# gravar o  dicionário do arquivo json
with open('cadastro.json', 'w') as arq:
# parametro = ........(dicionário, arq_json)
    json.dump(contato, arq)


# ler e imprimir o arquivo
with open('cadastro.json', 'r') as arq:
    # dicionário = .........(arq_json)
    dados_lidos = json.load(arq)
    print("Dados do arquivo Json")
    print(dados_lidos)

# exibir de maneira formatada
for k, v in dados_lidos.items():
    print(f"{k} -> {v}")

# modificando os dados de um arquivo json
with open('cadastro.json', 'r') as arq:
    dados_modificados = json.load(arq)

    # modificar os dados
    dados_modificados["idade"] = 30
    dados_modificados["cel"] = '12999999999'

# gravando o dicionário e gravando no arquivo
with open('cadastro.json', 'w') as arq:
    json.dump(dados_modificados, arq)

# lendo do arquivo os dados modificados
with open('cadastro.json', 'r') as arq:
    dados_modificados_lidos = json.load(arq)
    print("Arquivo Json modificado")
    print(dados_modificados_lidos)

# o idel seria usar o mesmo dicionário pra tudo
print(dados_lidos)
print(dados_modificados)
print(dados_modificados_lidos)