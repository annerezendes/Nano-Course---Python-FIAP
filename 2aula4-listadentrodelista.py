# dicionário e busca
import os
os.system("cls")

inventario = []
resposta = "S"

while resposta == "S":
    equipamento = [input("Equipamento: "), 
    float(input("Valor: ")),
    int(input("Número Serial: ")),
    input("Departamento: ")]

    inventario.append(equipamento)
    resposta = input("Digite [S]im para continuar: ").upper()

for elemento in inventario: 
    print(f"Nome...........: {elemento[0]}")         
    print(f"Valor..........: {elemento[1]}")         
    print(f"Serial.........: {elemento[2]}")         
    print(f"Departamento ..: {elemento[3]}")         

busca = input("\nDigite o equipamento que deseja buscar: ")
for elemento in inventario:
    if busca == elemento[0]:
        print(f"Valor...: {elemento[1]}")
        print(f"Serial..: {elemento[2]}")

depreciacao = input("\nDigite o nome do elemento a ser depreciado: ")
for elemento in inventario:
    if depreciacao == elemento [0]:
        print(f"Valor antigo: {elemento[1]}")
        elemento[1] = elemento[1] * 0.9
        print(f"Novo valor: {elemento[1]}")

serial = int(input("\n Digite o equipamento que será excluído: "))
for elemento in inventario: 
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print(f"Nome........: {elemento[0]}")
    print(f"Valor.......: {elemento[1]}")
    print(f"Serial......: {elemento[2]}")
    print(f"Departamento: {elemento[3]}")

valores = []
for elemento in inventario:
    valores.append(elemento[1])

if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))