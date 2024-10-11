import os
os.system("cls")

nome = input("Dgigite o nome do funcionário: ")
empresa = input("Digite o nome da empresa: ")
qtdFuncionarios = int(input("Digite a quantidade de funcionários da empresa: "))
mediaMensalidade = float(input("Digite a media mensal da sua empresa: "))

print("----------------------------------------------")

print(f"\n {nome} trabalha na empresa {empresa}")
print(f"\n A média da mensalidade é {mediaMensalidade}")
print(f"\n A quantidade de funcionário da {empresa} é {qtdFuncionarios}")