import os
os.system("cls")

# múltiplas listas e índices

equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Seriais: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar").upper()

# indices identificador do elemento da lista
# o len retorna o número de elementos presentes no objeto (nesse caso, a lista)
"""
ex: 
palavra = "Python"
tamanho = len(palavra)
print(tamanho) 
# saída: 6
"""
for indice in range (0, len(equipamentos)):
    print(f"\nEquipamentos..: {indice +1}")
    print(f"Nome..........: {equipamentos[indice]}")
    print(f"Valores.......: {valores[indice]}")
    print(f"Seriais.......: {seriais[indice]}")
    print(f"Departamento..: {departamento[indice]}")