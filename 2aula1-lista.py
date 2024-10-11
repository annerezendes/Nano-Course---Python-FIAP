import os
os.system("cls")

# lista que acumula dados inputados []

inventario = []
resposta = "S"
while resposta =="S" or resposta == "s":
    inventario.append(input("Equipamento: "))
    inventario.append(int(input("Quantidade de tópicos: ")))
   # print(inventario)
    resposta = input("\nDigite 'S' para continuar").upper()

# ele printa apenas quando o programa é encerrado
for elemento in inventario:
    print(elemento)