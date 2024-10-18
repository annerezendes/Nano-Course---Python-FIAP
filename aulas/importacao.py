import os
import pandas as pd
os.system("cls")
# pip install pandas openpyxl

# criando dicionário com alguns dados
dados = {
    'Nome' : ["Edson", "Esther", "Edilson"],
    'Idade' : [50, 60, 40],
    'Cidade' : ["Guarulhos", "São Paulo", "Belo Horizonte"]
}

# convertendo dicionário em um dataframe

df = pd.DataFrame(dados)

# salva o df em uma planilha do excel
nome_arquivo = "planilha.xlsx"
df.to_excel(nome_arquivo, index = False)
print(f"Arquivo {nome_arquivo} gerado!")