import os
os.system("cls")

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Seriais: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar ").upper()



busca = input("\nDigite o nome do equipamento que desja buscar: ")
for i in range (0, len(equipamentos)):
    if busca == equipamentos[i]:
        print(f"Valores ..: {valores[i]}")
        print(f"Seriais ..: {seriais[i]}")