from utilidades.funcoes import *

while True:
    opção = menu(['Tabuada fixa', 'Tabuada aleatoria', 'Encerrar o programa'])
    
    if opção == 1:
        tabuada_fixa()
    if opção == 2:
        tabuada_aleatoria()
    if opção == 3:
        break