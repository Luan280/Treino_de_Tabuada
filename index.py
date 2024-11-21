from unicodedata import digit

from utilidades.funcoes import *

while True:
    opcao = menu([
    'TREINAR TABUADA COM NÚMEROS FIXOS',
    'TREINAR TABUADA COM NÚMEROS ALEATÓRIOS',
    "TREINO DE SOMA COM NÚMEROS ALEATÓRIOS",
    'TREINO DE SUBTRAÇÃO COM NÚMEROS ALETÓRIOS',
    "TREINO DE MULTIPLICAÇÃO COM NÚMEROS ALEATÓRIOS",
    'ENCERRAR O PROGRAMA'])

    if opcao == 1:
        tabuada_fixa()
    elif opcao == 2:
        tabuada_aleatoria()
    elif opcao == 3:
        soma_simples()
    elif opcao == 4:
        subtracao_simples()
    elif opcao == 5:
        multiplicacao()
    elif opcao == 6:
        print(linha())
        print(colored("PROGRAMA FINALIZADO. VOLTE SEMPRE!", "yellow"))
        break
    else:
        text = 'ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4, 5, 6"'
        print(colored(f"{linha(len(text))}", "red"))
        print(colored(f"{text:^100}", "red"))
        print(colored(f"{linha(len(text))}", "red"))
