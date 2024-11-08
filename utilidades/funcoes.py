from random import randint
from time import sleep
from termcolor import colored


def linha(tam=40):
    return "-" * tam


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
        print(colored(f"\n{linha(76)}", "red"))
        print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
        print(colored(f"{linha(76)}", "red"))
        sleep(1.3)
        return 4
    except ValueError:
        print(colored(f"\n{linha()}", "red"))
        print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4"', "red"))
        print(colored(f"{linha()}", "red"))
        sleep(1.3)
    else:
        if resposta != 1 or 2 or 3 or 4:
            print(colored(f"\n{linha()}", "red"))
            print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4"', "red"))
            print(colored(f"{linha()}", "red"))
        return resposta


def tabuada_fixa():
    cabecalho(colored("TABUADAS COM NÚMEROS FIXOS [999 PARA SAIR]", 'blue'))
    while True:
        parada = False
        try:
            valor = int(input("DIGITE QUAL TABUADA VOCÊ QUER: "))
        except KeyboardInterrupt:
            print(colored(f"\n{linha(76)}", "red"))
            print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
            print(colored(f"{linha(76)}", "red"))
            sleep(1.3)
            break
        except ValueError:
            print(colored(f"\n{linha()}", "red"))
            print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!", "red"))
            print(colored(f"{linha()}", "red"))
        else:
            while True:
                print(linha())
                n1 = randint(1, 10)
                print(f"{valor} x {n1} = ", end="")
                try:
                    resposta = int(input(""))
                except ValueError:
                    print(colored(f"\n{linha()}", "red"))
                    print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!", "red"))
                    print(colored(f"{linha()}", "red"))
                except KeyboardInterrupt:
                    print(colored(f"\n{linha(76)}", "red"))
                    print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
                    print(colored(f"{linha(76)}", "red"))
                    sleep(1.3)
                    break
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        parada = True
                        return parada

                    if resposta == valor * n1:
                        print(colored("VOCÊ ACERTOU!", "green"))
                        sleep(1.3)
                    else:
                        print(colored("VOCÊ ERROU!", "red"))
                        print(f"A RESPOSTA CORRETA É {valor * n1}.")
                    sleep(1.3)
        if parada:
            break


def tabuada_aleatoria():
    while True:
        quebra = False
        try:
            cabecalho(colored("TABUADA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]", 'blue'))
            limite = int(input("Digite o valor máximo da tabuada: "))
        except ValueError:
            print("Digite somente números inteiros.")
        else:
            while True:
                n1 = randint(1, int(limite))
                n2 = randint(1, int(limite))
                print(f"{n1} x {n2} = ", end="")
                try:
                    resposta = int(input(""))
                except KeyboardInterrupt:
                    print(colored(f"\n{linha(76)}", "red"))
                    print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
                    print(colored(f"{linha(76)}", "red"))
                    sleep(1.3)
                    quebra = True
                    break
                except ValueError:
                    print(colored(f"\n{linha()}", "red"))
                    print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!", "red"))
                    print(colored(f"{linha()}", "red"))
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        quebra = True
                        break
                    elif resposta == n1 * n2:
                        print(colored("VOCÊ ACERTOU!", "green"))
                        print(linha())
                        sleep(1.3)
                    else:
                        print(colored("VOCÊ ERROU!", 'red'))
                        print(f"A RESPOSTA CORRETA É {n1*n2}.")
                        print(linha())
                        sleep(1.3)
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
            print(colored(f"\n{linha()}", "red"))
            print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!", "red"))
            print(colored(f"{linha()}", "red"))
        except KeyboardInterrupt:
            print(colored(f"\n{linha(76)}", "red"))
            print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
            print(colored(f"{linha(76)}", "red"))
            sleep(1.3)
            quebra = True
            break
        else:
            while True:
                n1 = randint(0,int(limite))
                n2 = randint(0, int(limite))
                print(f" {n1}\n {n2} +\n------")
                try:
                    resposta = int(input(""))
                except ValueError:
                    print(colored(f"\n{linha()}", "red"))
                    print(colored("ERRO: DIGITE SOMENTE NÚMEROS INTEIROS!", "red"))
                    print(colored(f"{linha()}", "red"))
                except KeyboardInterrupt:
                    print(colored(f"\n{linha(76)}", "red"))
                    print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
                    print(colored(f"{linha(76)}", "red"))
                    sleep(1.3)
                    quebra = True
                    break
                else:
                    if resposta == 999:
                        print(colored("VOLTANDO PARA O MENU PRINCIPAL....", 'red'))
                        sleep(1.3)
                        quebra = True
                        break
                    elif resposta == n1+n2:
                        print(colored("VOCÊ ACERTOU!", "green"))
                        print(linha())
                        sleep(1.3)
                    else:
                        print(colored("VOCÊ ERROU!", 'red'))
                        print(f"A RESPOSTA CORRETA É {n1 + n2}.")
                        print(linha())
                        sleep(1.3)
        if quebra:
            break