import os
os.system("cls")

with open("4aula1-arq", "r") as file:
    conteudo = file.readline()
    for linha in file.readlines():
        print(linha)