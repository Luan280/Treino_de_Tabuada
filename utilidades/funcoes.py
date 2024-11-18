from random import randint
from time import sleep
from termcolor import colored


def linha(tam=30):
    return ("-" * tam) * 2


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
    text = "VOCÊ ERROU!"
    text2 = f"A RESPOSTA CORRETA É {total}."
    print(colored(f"{linha(len(text2))}", "red"))
    print(colored(f"{text:^43}", "red"))
    print(f"{text2:^43}")
    print(colored(f"{linha(len(text2))}", "red"))
    sleep(1.3)


def you_win():
    text = "VOCÊ ACERTOU!"
    print(colored(f"{linha(len(text))}", "green"))
    print(colored(f"{text:^26}", "green"))
    print(colored(f"{linha(len(text))}","green"))
    sleep(1.3)

def back_menu():
    text = "VOLTANDO PARA O MENU PRINCIPAL...."
    print(colored(f"{linha(len(text))}","yellow"))
    print(colored(f"{text:^68}", 'yellow'))
    print(colored(f"{linha(len(text))}","yellow"))
    sleep(1.3)



def cabecalho(texto):
    texto_size = len(texto) * 2
    print(colored(f"{linha(len(texto))}","blue"))
    print(colored(f"{texto:^{texto_size}}", "blue"))
    print(colored(f"{linha(len(texto))}","blue"))


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 0
    for valor in lista:
        c += 1
        print(colored(f"{c} - {valor}", "yellow"))
    print(linha())
    try:
        resposta = int(input("DIGITE UMA DAS OPÇÔES (1, 2, 3, 4, 5, 6): "))
        print(linha())
    except KeyboardInterrupt:
        keyboard_interrupt()
        return 6
    except ValueError:
        print(colored(f"\n{linha()}", "red"))
        print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4, 5, 6"', "red"))
        print(colored(f"{linha()}", "red"))
        sleep(1.3)
    else:
        return resposta



def tabuada_fixa():
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
                cabecalho("TABUADAS COM NÚMEROS FIXOS [999 PARA SAIR]")
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
                        back_menu()
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
            cabecalho("TABUADA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
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
                        back_menu()
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
            cabecalho("SOMA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
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
                        back_menu()
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
            cabecalho("SOMA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
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
                        back_menu()
                        quebra = True
                        break
                    elif resposta == total:
                        you_win()
                    else:
                        you_lose(total)
        if quebra:
            break


def multiplicacao():
    cabecalho("MULTIPLICAÇÃO COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
    try:
        limite = int(input("Digite o valor máximo da multiplicação: "))
    except ValueError:
        value_error()
    except KeyboardInterrupt:
        keyboard_interrupt()
    else:
        n1 = randint(1, int(limite))
        n2 = randint(1, int(limite))
        print(f"{n1}\n{n2} *")
