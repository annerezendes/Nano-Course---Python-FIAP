import os 
os.system("cls")

numero = int(input("Número: "))

for i in range (1, 11, 1):
    tabuada = numero*i
    print(f"{numero} x {i} = {tabuada}")