import os
import pandas as pd
import oracledb
os.system("cls")


# Conexão com o Banco de Dados
try:
    conn = oracledb.connect(user="RM556779", password="150306", dsn='oracle.fiap.com.br:1521/ORCL')

    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
except Exception as e:
    print("Erro ao conectar: ", e)
    conexao = False
else:
    conexao = True
    
    
def exibirMenu():
    while True: 
        print(f"""
          0 - SAIR
          1 - CADASTRAR
          2 - LISTAR E EXPORTAR
          """)
        opcao = input("\nDigite o número da opção: ")
        match opcao:   
            case '0':
                sair()
                break
            case '1':
                cadastrar()
            case '2':
                listarExportar()
            case _:
                print("Digite uma opção válida!")
            
def sair():
    resposta = input("Pressione S para sair ")
    if resposta == 'S' or resposta == 's':
        print("Obrigado por utilizar a nossa aplicação! :)")

def cadastrar():
    
    print("\n----- Cadastrar Artista -----")
    nome = input("\nDigite o nome.......: ")    
    genero_musical = input("Digite gênero.......: ")
    try:
        cadastro = f""" INSERT INTO CP_ARTISTA (nome, genero_musical) VALUES ('{nome}', '{genero_musical}') """

        inst_cadastro.execute(cadastro)
        conn.commit()
    except:
        # Caso ocorra algum erro de conexão ou no BD
        print("Erro na transação do BD")
    else:
        # Caso haja sucesso na gravação
        print("----- Dados gravados :) -----")
        
def listarExportar():
    print("\n----- Listar Usuários -----")
    lista_dados = [] 
    inst_consulta.execute('SELECT * FROM CP_ARTISTA')

    data = inst_consulta.fetchall()
    for dt in data:
        lista_dados.append(dt)
    lista_dados = sorted(lista_dados)
    
    # convertendo para um dicionário 
    dados_df = pd.DataFrame(lista_dados)
    if dados_df.empty:
        print(f"Não há Usuários cadastrados!")
    else:
        print(dados_df)
        tabela = 'planilha_artista.xlsx'
        dados_df.to_excel(tabela, index = False)
        print(f"\nArquivo {tabela} gerado!")
        
# ---------- pp
exibirMenu()
            