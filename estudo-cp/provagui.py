# Anne Rezendes e Guilherme AKira


import os
os.system("cls")

prova = {
    "q1": {
        "enun": "1. Qual desses números é múltiplo de 3?",
        "alternativa": {
            "a": 11,
            "b": 27,
            "c": 40
        },
        "resp": "b"
    },
    "q2": {
        "enun": "2. Qual desses números é primo?",
        "alternativa": {
            "a": 2,
            "b": 4,
            "c": 6
        },
        "resp": "a"
    },
    "q3": {
        "enun": "3. Qual número é um quadrado perfeito?",
        "alternativa": {
            "a": 27,
            "b": 18,
            "c": 25
        },
        "resp": "c"
    },
    "q4": {
        "enun": "4. Qual a raiz cúbica de 27?",
        "alternativa": {
            "a": 3,
            "b": 9,
            "c": 18
        },
        "resp": "a"
    },
    "q5": {
        "enun": "5. Quanto é 35% de 50?",
        "alternativa": {
            "a": 17.5,
            "b": 27.3,
            "c": 35.5
        },
        "resp": "a"
    }
}


def fazerProva() -> int:
    acertos = 0
    for questao, pergunta in prova.items():
        print(f"{pergunta['enun']}")
        for alternativa, resposta in prova[questao]['alternativa'].items():
            print(f"{alternativa}) {resposta}")
        resp = input("Digite sua resposta: ").lower()
        if resp == prova[questao]['resp']:
            print("Resposta CORRETA!!!\n")
            acertos +=1
        else:
            print("Resposta INCORRETA :(\n")
    return acertos

def exibeResultado(n: int, p:int):
    pergunta = "perguntas"
    if n == 1:
        pergunta = "pergunta"
    print(f"""
Você acertou {n} {pergunta}.
Sua porcentagem de acertos foi {p}%.      
      """)
    
def verGabarito():
    while True:
        opc = input("Você gostaria de conferir o gabarito?(S/N) ").upper()
        nPergunta = 1
        if opc == "S":
            for pergunta in prova.values():
                print(f"{nPergunta}. {pergunta['resp']}")
                nPergunta +=1
            break
        elif opc == "N" :
            break
        else:
            print("Opção inválida!\n")

def main():
    acertos = fazerProva()
    porcent_acertos = (acertos / len(prova)) * 100
    porcent_acertos = int(porcent_acertos)
    exibeResultado(acertos, porcent_acertos)
    verGabarito()
    print("\nSISTEMA ENCERRANDO...")

#PROGRAMA PRINCIPAL
main()