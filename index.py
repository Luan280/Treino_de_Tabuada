from utilidades.funcoes import *

while True:
    opcao = menu([colored('TREINAR TABUADA COM NÚMEROS FIXOS', 'yellow'),
    colored('TREINAR TABUADA COM NÚMEROS ALEATÓRIOS', 'yellow'),
    colored('TREINO DE SOMA COM NÚMEROS ALETÓRIOS', 'yellow'),
    colored('TREINO DE SUBTRAÇÃO COM NÚMEROS ALETÓRIOS', 'yellow'),
    colored("TREINO DE MULTIPLICAÇÃO COM NÚMEROS ALEATÓRIOS", "yellow"),
    colored('ENCERRAR O PROGRAMA', 'yellow')])
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
        print(colored(f"{linha()}", "red"))
        print(colored('ERRO: DIGITE SOMENTE AS OPÇÕES: "1, 2, 3, 4"', "red"))
        print(colored(f"{linha()}", "red"))