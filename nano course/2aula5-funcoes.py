import os
os.system("cls")


# quebrar o script em vários módulos diferentes

inventario = []
resposta = "S"

def preencher():
    while resposta == "S":
        equipamento = [input("Equipamento: "), 
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")]

        inventario.append(equipamento)
        resposta = input("Digite [S]im para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista: 
        print(f"Nome...........: {elemento[0]}")         
        print(f"Valor..........: {elemento[1]}")         
        print(f"Serial.........: {elemento[2]}")         
        print(f"Departamento ..: {elemento[3]}")         

def localizarPorNome(lista):
    busca = input("\nDigite o equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print(f"Valor...: {elemento[1]}")
            print(f"Serial..: {elemento[2]}")

def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do elemento a ser depreciado: ")
    for elemento in lista:
        if depreciacao == elemento [0]:
            print(f"Valor antigo: {elemento[1]}")
            elemento[1] = elemento[1] * (1 - porc/100)
            print(f"Novo valor: {elemento[1]}")

def excluirPorSerial(lista):
    serial = int(input("\n Digite o equipamento que será excluído: "))
    for elemento in lista: 
        if elemento[2] == serial:
            inventario.remove(elemento)
    return "Itens excuídos." 

def exibindo():
    for elemento in inventario:
        print(f"Nome........: {elemento[0]}")
        print(f"Valor.......: {elemento[1]}")
        print(f"Serial......: {elemento[2]}")
        print(f"Departamento: {elemento[3]}")


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

# ------- programa principal

minhaLista = []
print("Preenchendo")
preencher(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)

print("Excluindo")
excluirPorSerial(minhaLista)
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)