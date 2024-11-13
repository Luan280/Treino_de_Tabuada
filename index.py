from utilidades.funcoes import *

while True:
    opcao = menu([colored('TREINAR TABUADA COM NÚMEROS FIXOS', 'yellow'),
    colored('TREINAR TABUADA COM NÚMEROS ALEATÓRIOS', 'yellow'),
    colored('TREINO DE SOMA COM NÚMEROS ALETÓRIOS', 'yellow'),
    colored('TREINO DE SUBTRAÇÃO COM NÚMEROS ALETÓRIOS', 'yellow') ,
    colored('ENCERRAR O PROGRAMA', 'yellow')])
    if opcao == 1:
        tabuada_fixa()
    if opcao == 2:
        tabuada_aleatoria()
    if opcao == 3:
        soma_simples()
    if opcao == 4:
        subtracao_simples()
    if opcao == 5:
        print(linha())
        print(colored("PROGRAMA FINALIZADO. VOLTE SEMPRE!", "yellow"))
        break