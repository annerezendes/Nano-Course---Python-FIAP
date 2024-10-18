import os
os.system("cls")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Acesso liberado! {nome} é maior de idade!")
else: 
    print("Acesso negado...")
print("\nSistema encerrando ... ")