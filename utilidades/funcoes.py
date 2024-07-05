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
        c += 1
        print(f"{c} - {valor}")
    print(linha())
    try:
        resposta = int(input("Digite uma das opções (1, 2, 3): "))
    except KeyboardInterrupt:
        print(f"\n{linha(76)}")
        print("ERRO: Já que nenhum valor foi informado, estamos encerrando o sistema...... ")
        print(linha(76))
        sleep(2)
        return 3

    except ValueError:
        print(linha())
        print('\n1ERRO: Digite Somente as opções "1, 2, 3"')
        print(linha())
        sleep(2)
    else:
        return resposta


def tabuada_fixa():
    cabeçalho("TABUADAS FIXAS [999 PARA SAIR]")
    while True:
        parada = False
        try:
            valor = int(input("Digite o número da tabuada fixa: "))
        except KeyboardInterrupt:
            print(f"\n{linha(76)}")
            print("ERRO: Já que nenhum valor foi informado, estamos encerrando o sistema......")
            print(linha(76))
            sleep(1.5)
            break
        except ValueError:
            print(f"\n{linha()}")
            print("ERRO: Digite somente NÚMEROS!")
            print(linha())
        else:
            while True:
                print(linha())
                n1 = randint(1, 10)
                print(f"{valor} x {n1} = ", end="")
                resposta = int(input(""))
                if resposta == 999:
                    parada = True
                    return parada

                if resposta == valor * n1:
                    print("Você ACERTOU!")
                    sleep(1.5)
                else:
                    print("Você ERROU!")
                    print(f"A resposta correta é {valor * n1}.")
                sleep(1.5)
        if parada:
            break


def tabuada_aleatoria():
    global resposta
    cabeçalho("TABUADAS ALEATÓRIAS [999 PARA SAIR]")
    while True:
        try:
            resposta = int(input(""))
        except KeyboardInterrupt:
            print(f"\n{linha(76)}")
            print("ERRO: Já que nenhum valor foi informado, estamos encerrando o sistema......")
            print(linha(76))
            break
        except ValueError:
            print(f"\n{linha()}")
            print("ERRO: Digite somente números!")
            print(linha())
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        print(f"{n1} x {n2} = ", end="")
        if resposta == 999:
            break
        if resposta == n1 * n2:
            print("Você ACERTOU!")
            print(linha())
            sleep(1.5)
        else:
            print("Você ERROU!")
            print(f"A resposta correta é {n1*n2}.")
            print(linha())
            sleep(1.5)
