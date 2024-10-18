import os
os.system("cls")

# tupla é imutável, não dá pra manipular os valores

usuarios = {}
emails = ["anne@gmail.com", "cloe@fiap.com"]

tupla = list(enumerate(emails))
# print(tupla)

for chave in range (0, len(tupla)):
    # 0 até o tamanho da tupla
    print(f"E-mail: {tupla[chave][1]}")
    usuarios[tupla[chave]] = input("Digite o nome: "), input("Digite o nível: ")

for chave, dado in usuarios.items():
    print(f"Usuário.: {chave[0]}")
    print(f"E-mail..: {chave[1]}")
    print(f"Nome....: {chave[0]}")
    print(f"Nível...: {chave[1]}")