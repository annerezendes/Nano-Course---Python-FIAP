import os
os.system("cls")

usuarios = {}

# ------- sub

def perguntar():
    return input("O que deseja realizar?\n" +
              "[I] - Para Inserir um usuário" +
              "[P] - Para Pesquisar um usuário" +
              "[E] - Para Excluir um usuário" +
              "[L] - Para Listar um usuário: ").upper()

     
def inserir(dict):
    dict[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(), input("Digite a última data de acesso: "), input("Qual a última estação acessada: ").upper()]


# ------- principal

opcao = perguntar()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)