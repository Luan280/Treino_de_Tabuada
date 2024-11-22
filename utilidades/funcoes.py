from random import randint
from time import sleep
from termcolor import colored

from testes import sorted_number


def linha(tam=30):
    """Função que retorna uma linha"""
    return ("-" * tam) * 2

def random_numbers(limit_account):
    number_1 = randint(0, int(limit_account))
    number_2 = randint(0, int(limit_account))
    return number_1, number_2

def keyboard_interrupt():
    """Função que exibi uma mensagem de erro quando entra em um except de 'KeyboardIterrupt'"""
    print(colored(f"\n{linha(76)}", "red"))
    print(colored("ERRO: JÁ QUE NENHUM VALOR FOI INFORMADO, ESTAMOS ENCERRANDO O SISTEMA...", "red"))
    print(colored(f"{linha(76)}", "red"))
    sleep(1.3)


def value_error():
    """Função que exibi uma mensagem de erro quando entra em um except de 'ValueError'"""
    text = "ERRO: DIGITE SOMENTE NÚMEROS INTEIROS."
    print(colored(f"{linha(len(text))}", "red"))
    print(colored(f"{text:^70}", "red"))
    print(colored(f"{linha(len(text))}", "red"))

def you_lose(total):
    """Função que exibi uma mensagem mostrando que você errou a resposta e mostra o resultado correto"""
    text = "VOCÊ ERROU!"
    text2 = f"A RESPOSTA CORRETA É {total}."
    print(colored(f"{linha(len(text2))}", "red"))
    print(colored(f"{text:^43}", "red"))
    print(f"{text2:^43}")
    print(colored(f"{linha(len(text2))}", "red"))
    sleep(1.3)


def you_win():
    """Funçãp que mostra uma mensagem mostrando que você acertou a questão"""
    text = "VOCÊ ACERTOU!"
    print(colored(f"{linha(len(text))}", "green"))
    print(colored(f"{text:^26}", "green"))
    print(colored(f"{linha(len(text))}","green"))
    sleep(1.3)

def back_menu():
    """Função que mostra uma mensagem"""
    text = "VOLTANDO PARA O MENU PRINCIPAL...."
    print(colored(f"{linha(len(text))}","yellow"))
    print(colored(f"{text:^68}", 'yellow'))
    print(colored(f"{linha(len(text))}","yellow"))
    sleep(1.3)



def cabecalho(texto):
    """Função que gera uma cabeçalho para todos os sistemas"""
    texto_size = len(texto) * 2
    print(colored(f"{linha(len(texto))}","blue"))
    print(colored(f"{texto:^{texto_size}}", "blue"))
    print(colored(f"{linha(len(texto))}","blue"))


def menu(lista):
    """Função que mostra um menu de opções de sistemas"""
    cabecalho("MENU PRINCIPAL")
    c = 0
    for valor in lista:
        c += 1
        print(colored(f"{c} - {valor}", "yellow"))
    print(linha())
    try:
        resposta = int(input("DIGITE UMA DAS OPÇÔES (1, 2, 3, 4, 5, 6): "))
    except KeyboardInterrupt:
        keyboard_interrupt()
        return 6
    except ValueError:
        value_error()
    else:
        return resposta



def tabuada_fixa():
    """Função que gera uma tabuada com números que o usuário escolher"""
    while True:
        break_loop = False
        try:
            multiplication_table = int(input("DIGITE QUAL TABUADA VOCÊ QUER: "))
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        except ValueError:
            value_error()
        else:
            while True:
                cabecalho("TABUADAS COM NÚMEROS FIXOS [999 PARA SAIR]")
                number_1, *_ = random_numbers(multiplication_table)
                total = multiplication_table * number_1
                print(f"{multiplication_table} x {number_1} = ", end="")
                try:
                    user_response = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    break
                else:
                    if user_response == 999:
                        back_menu()
                        break_loop = True
                        return break_loop

                    if user_response == total:
                        you_win()
                    else:
                        you_lose(total)
        if break_loop:
            break


def tabuada_aleatoria():
    """Função que gera uma tabuada com números aleatórios"""
    while True:
        break_loop = False
        try:
            cabecalho("TABUADA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
            limit_account = int(input("DIGITE O VALOR MÁXIMO DA TABUADA: "))
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                number_1, number_2 = random_numbers(limit_account)
                total = number_1 * number_2
                print(f"{number_1} x {number_2} = ", end="")
                try:
                    user_response = int(input(""))
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    break_loop = True
                    break
                except ValueError:
                    value_error()
                else:
                    if user_response == 999:
                        back_menu()
                        break_loop = True
                        break
                    elif user_response == total:
                        you_win()
                    else:
                        you_lose(total)
        if break_loop:
            break


def soma_aleatoria():
    """Função que mostra uma conta de soma aleatória"""
    while True:
        break_loop = False
        try:
            cabecalho("SOMA COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
            limit_account = int(input("DIGITE O VALOR MÁXIMO DA SOMA: "))
            print(linha())
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                number_1, number_2 = sorted_number(limit_account)
                total = number_1 + number_2
                print(f" {number_1}\n {number_2} +\n------")
                try:
                    user_response = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    break_loop = True
                    break
                else:
                    if user_response == 999:
                        back_menu()
                        break_loop = True
                        break
                    elif user_response == total:
                        you_win()
                    else:
                        you_lose(total)
        if break_loop:
            break


def subtracao_aleatoria():
    """Função que mostra uma conta de subtração com números aleatórios"""
    while True:
        break_loop = False
        try:
            cabecalho("SUBTRAÇÃO COM NÚMEROS ALEATÓRIOS [999 PARA SAIR]")
            limit_account = int(input("DIGITE O VALOR MÁXIMO DA SUBTRAÇÃO: "))
            print(linha())
        except ValueError:
            value_error()
        except KeyboardInterrupt:
            keyboard_interrupt()
            break
        else:
            while True:
                number_1, number_2 = random_numbers(limit_account)
                total = number_1 - number_2
                print(f" {number_1}\n {number_2} -\n------")
                try:
                    user_response = int(input(""))
                except ValueError:
                    value_error()
                except KeyboardInterrupt:
                    keyboard_interrupt()
                    break_loop = True
                    break
                else:
                    if user_response == 999:
                        back_menu()
                        break_loop = True
                        break
                    elif user_response == total:
                        you_win()
                    else:
                        you_lose(total)
        if break_loop:
            break


def multiplicacao():
    """Função que mostra uma conta de multiplicação"""
    cabecalho("MULTIPLICAÇÃO COM NÚMEROS ALEATÓRIOS[999 PARA SAIR]")
    try:
        limit_account = int(input("DIGITE O VALOR MÁXIMO DA MULTIPLICAÇÃO: "))
    except ValueError:
        value_error()
    except KeyboardInterrupt:
        keyboard_interrupt()
    else:
        while True:
            number_1, number_2 = random_numbers(limit_account)
            total = number_1 * number_2
            print(f"{number_1}\n{number_2} *\n------")
            try:
                user_response = int(input(""))
            except ValueError:
                value_error()
            except KeyboardInterrupt:
                keyboard_interrupt()
                break
            else:
                if user_response == 999:
                    back_menu()
                    break
                elif user_response == total:
                    you_win()
                else:
                    you_lose(total)