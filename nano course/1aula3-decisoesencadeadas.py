import os
os.system("cls")

# atendimento prioritário - idade e contagio
nome = input("Nome: ")
idade = int(input("Idade: "))
doencaC = input("Suspeita de doença infeccontagiosa? ")

if idade >= 65:
    print(f"O paciente {nome} POSSUI atendimento prioritário!")
elif doencaC =="SIM" or doencaC =="sim":
    print(f"O paciente {nome} deve ser encaminhado para a sala reservada.")
else:
    print(f"O paciente {nome} NÃO POSSUI atendimento prioritário. Dirija-se a sala comum.")