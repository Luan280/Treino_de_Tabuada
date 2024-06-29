from random import randint
from time import sleep

def linha(tam=30):
    return "-" * tam
    
def cabeçalho(texto):
    print(linha())
    print(texto.center(30))
    print(linha())

def menu():
    print("""1- Tabuada com valor fixo
2- Tabuada com valores aleátórios
3 - sair do sistema""")
    print(linha())

def tabuada():
    while True:
        menu()
        opção = int(input("Digite qual opção você quer: "))
        print(linha())
        if opção == 1:
            valor = int(input("Digite o valor da tabuada que você quer em especifico: "))
            print(linha())
            n1 = randint(1, 10)
            print(f"{valor} x {n1} = ", end="")
            resposta = int(input(""))
            if resposta == valor * n1:
                print("Você ACERTOU!")
            else:
                print("Você ERROU!")

        if opção == 2:
            n1 = randint(1, 10)
            n2 = randint(1, 10)
            print(f"{n1} x {n2} = ", end="")
            resposta = int(input(""))
            if resposta == n1 * n2:
                print("Você ACERTOU!")
            else:
                print("Você ERROU!")
        if opção == 3:
            break