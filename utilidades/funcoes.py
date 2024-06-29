from random import randint
from time import sleep

def linha(tam=40):
    return "-" * tam
    
def cabeçalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 0
    for valor in lista:
        c +=1
        print(f"{c}- {valor}")
    print(linha())
    resposta = int(input("Digite qual opção você quer: "))
    return resposta

def tabuada_fixa():
    cabeçalho("TABUADAS FIXAS [999 PARA SAIR]")
    valor = int(input("Digite o valor fixo: "))
    while True:
        print(linha())
        n1 = randint(1, 10)
        print(f"{valor} x {n1} = ", end="")
        resposta = int(input(""))

        if resposta == valor * n1:
            print("Você ACERTOU!")
            sleep(1.5)
        else:
            print("Você ERROU!")
            print(f"A resposta correta é {valor * n1}.")
            sleep(1.5)
        if resposta == 999:
            break
        

def tabuada_aleatoria():
    cabeçalho("TABUADAS ALEATÓRIAS [999 PARA SAIR]")
    while True:
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        print(f"{n1} x {n2} = ", end="")
        resposta = int(input(""))
        if resposta == n1 * n2:
            print("Você ACERTOU!")
            print(linha())
            sleep(1.5)
        else:
            print("Você ERROU!")
            print(f"A resposta correta é {n1*n2}.")
            print(linha())
            sleep(1.5)
        if resposta == 999:
            break