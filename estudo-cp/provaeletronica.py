import os
os.system("cls")

# dicionario principal 

prova = {

    # key1
    'Pergunta 1':
    {
        #key1a
        'enunciado': 'Qual desses números é múltiplo de 3?', 
        # key 1ab
        'alternativas':
        {
            'a': 27,
            'b': 13,
            'c': 23
        },

        'resposta_certa': 'a'
    },

    'Pergunta 2':
    {
        'enunciado': 'Qual desses números é primo?', 'alternativas':
        {
            'a': 4,
            'b': 2,
            'c': 10

        },

        'resposta_certa' : 'b'
    },

    'Pergunta 3':
    {
        'enunciado': 'Qual número é um quadrado perfeito?', 'alternativas':
        {
            'a': 27,
            'b': 30,
            'c': 36
        },

        'resposta_certa': 'c'
    },

    'Pergunta 4':
    {
        'enunciado': 'Qual a raiz cúbica de 27?', 'alternativas': 
        {
            'a': 9,
            'b': 7,
            'c': 3
        },

        'resposta_certa': 'c'
    },

    'Pergunta 5':
    {
        'enunciado': 'Quanto é 2 x 3?', 'alternativas':
        {
            'a': 8,
            'b': 9,
            'c': 6
        },

        'resposta_certa': 'c'
    }
}

import os
os.system("cls")

# acertos = 0 até que prove o contrário
acertos = 0

"""
pergunta = nome dos itens de prova(l) - Pergunta 1, 2.,...
dados_pergunta = enunciado 
resposta = alternativas 
dados_resposta = dict a,b,c
prova.items = tudo: pergunta + enunciado + alternativas + resposta_certa
"""
# exibindo perguntas e enunciado
for pergunta, dados_pergunta in prova.items():
    print(f"{pergunta}:\n\t{dados_pergunta['enunciado']}")

    # exibindo as alternativas
    for resposta, dados_resposta in dados_pergunta['alternativas'].items():
        print(f"\t\t{resposta}) {dados_resposta}")
    
    # le resposta do usuário:
    resposta = input("\n Sua resposta: ")

    # verifica se acertou ou não
    if resposta == dados_pergunta['resposta_certa']:
            print("Parabéns. Resposta correta!")
            acertos +=1
    else:
            print("Incorreto :(")
    
    print( )

# mostra a nota 
quantidade_perguntas = len(prova)
porcentagem_acerto = acertos / quantidade_perguntas * 100
# risco
print('-'*40)
print(f"\nVocê acertou {acertos}/{quantidade_perguntas}", end = ' ')

# operador ternário
# <comando verdade> if <condicao> else <comando falso>
print("perguntas.") if acertos > 1 or acertos <= 0 else print("pergunta.")
print(f"Sua porcentagem foi de {porcentagem_acerto} :)")