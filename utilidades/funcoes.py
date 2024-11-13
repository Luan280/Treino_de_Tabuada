from random import randint
from time import sleep
from termcolor import colored


def linha(tam=40):
    return "-" * tam


def keyboard_interrupt():
    print(colored(f"\n{linha(76)}", "red"))
    print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
    print(colored(f"{linha(76)}", "red"))
    sleep(1.3)


def value_error():
    print(colored(f"\n{linha()}", "red"))
    print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS.", "red"))
    print(colored(f"{linha()}", "red"))

def you_lose(total):
    print(colored("VOCÊ ERROU!", "red"))
    print(f"A RESPOSTA CORRETA É {total}.")
    sleep(1.3)


def you_win():
    print(colored(linha(20)))
    print(colored("VOCÊ ACERTOU!", "green"))
    print(colored(linha(20)))
    sleep(1.3)


def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())


def menu(lista):
    cabecalho(colored("   MENU PRINCIPAL", 'blue'))
    c = 0
    for valor in lista:
        c += 1
        print(colored(f"{c} - {valor}", "yellow"))
    print(linha())
    try:
        resposta = int(input("DIGITE UMA DAS OPÇÔES (1, 2, 3, 4): "))
    except KeyboardInterrupt:
        keyboard_interrupt()
        return 5
    except ValueError:
        print(colored(f"\n{linha()}", "red"))
        print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4"', "red"))
        print(colored(f"{linha()}", "red"))
        sleep(1.3)
    else:
        if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4 or resposta == 5 or resposta == 6:
            return resposta
        else:
            print(colored(f"\n{linha()}", "red"))
            print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4"', "red"))
            print(colored(f"{linha()}", "red"))


def tabuada_fixa():
    cabecalho(colored("TABUADAS COM NÚMEROS FIXOS [999 PARA SAIR]", 'blue'))
    while True:
        parada = False
        try:
            valor = int(input("DIGITE QUAL TABUADA VOCÊ QUER: "))
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        except ValueError:
            value_error()
        else:
            while True:
                print(linha())
                n1 = randint(1, 10)
                total = valor * n1
                print(f"{valor} x {n1} = ", end="")
                try:
                    resposta = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    break
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        parada = True
                        return parada

                    if resposta == total:
                        you_win()
                    else:
                        you_lose(total)
        if parada:
            break


def tabuada_aleatoria():
    while True:
        quebra = False
        try:
            cabecalho(colored("TABUADA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]", 'blue'))
            limite = int(input("Digite o valor máximo da tabuada: "))
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                n1 = randint(1, int(limite))
                n2 = randint(1, int(limite))
                total = n1 * n2
                print(f"{n1} x {n2} = ", end="")
                try:
                    resposta = int(input(""))
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    quebra = True
                    break
                except ValueError:
                    value_error()
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        quebra = True
                        break
                    elif resposta == total:
                        you_win()
                    else:
                        you_lose(total)
        if quebra:
            break


def soma_simples():
    while True:
        quebra = False
        try:
            cabecalho(colored("SOMA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]", 'blue'))
            limite = int(input("Digite o valor máximo da soma: "))
            print(linha())
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                n1 = randint(0, int(limite))
                n2 = randint(0, int(limite))
                total = n1 + n2
                print(f" {n1}\n {n2} +\n------")
                try:
                    resposta = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    quebra = True
                    break
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        quebra = True
                        break
                    elif resposta == total:
                        you_win()
                    else:
                        you_lose(total)
        if quebra:
            break


def subtracao_simples():
    while True:
        quebra = False
        try:
            cabecalho(colored("SOMA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]", 'blue'))
            limite = int(input("Digite o valor máximo da subtração: "))
            print(linha())
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                n1 = randint(0, int(limite))
                n2 = randint(0, int(limite))
                total = n1 - n2
                print(f" {n1}\n {n2} -\n------")
                try:
                    resposta = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    quebra = True
                    break
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        quebra = True
                        break
                    elif resposta == total:
                        you_win()
                    else:
                        you_lose(total)
        if quebra:
            break


def multiplicacao():
    cabecalho(colored("MULTIPLICAÇÃO COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]", 'blue'))
    try:
        limite = int(input("Digite o valor máximo da tabuada: "))
    except ValueError:
        print("Digite somente números inteiros.")
    except KeyboardInterrupt:
        print(colored(f"\n{linha(76)}", "red"))
        print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
        print(colored(f"{linha(76)}", "red"))
        sleep(1.3)
