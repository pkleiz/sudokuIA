# programa para criar um tabuleiro completo de sudoku
# resolvendo sudoku usando hillclimbing
# CopyRight Pedro Kleiz e Gabriel Luna
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀ ⠈⢻⣿⣿⡄⠀
#⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀ ⠀⠀⠈⠙⢿⣷⡄⠀
#⠀⠀⣀⣤⣴⣶⣿⡟⠀ ⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀⣿⣷⠀
#⠀⢰⣿⡟⠋⠉⣹⣿ ⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
#⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
#⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
#⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⣿⣧⠀
#⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⣿⣿⠀⠀ ⠀
# ⣿⣿⠀⠀⠀⣿⣿⡇⠀                 ⢸⣿⣿⠀⠀
#⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
#⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⣿⣿⠃
#⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀ ⢸⣿⡇⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀ ⠀⣸⣿⠇⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⠁ ⠈⠻⣿⣿⣿⣿⡿⠏⠀
#⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀
#------------------------------------------------------------

from random import *

#funcao principal que inicia o programa
def sudokuBolado():
    solucao = geraSolucaoAleatoria()
    pontuacaoSolucao = avaliaSolucao(solucao)
    
    contadorDeRodadas = 0
    while True:
        contadorDeRodadas+=1
        print("Melhor pontuacao ate agora - ", pontuacaoSolucao,
              "\n         Solucao ")
        for i in range(9):
            print(solucao[i],"\n")
        print("Rodada Atual: ",contadorDeRodadas,"\n \n")
        if pontuacaoSolucao == 0:
            break

        novaSolucao = solucao
        aceitaSolucaoMelhor(novaSolucao)

        pontuacao = avaliaSolucao(novaSolucao)

        if avaliaSolucao(novaSolucao) < pontuacaoSolucao:
            solucao = novaSolucao
            pontuacaoSolucao = pontuacao
    
    
#gera solucao aleatoria onde as constantes nao se modificam
def geraSolucaoAleatoria():
    tabuleiro = []
    #criando tabuleiro previamente preenchido
    for i in range(1,10):
        linha = []
        for j in range(1,10):
            if(i == 1 and j == 4):
                linha.append(7)
            elif(i == 2 and j == 1):
                linha.append(1)
            elif(i == 3 and j == 4):
                linha.append(4)
            elif(i == 3 and j == 5):
                linha.append(3)
            elif(i == 3 and j == 7):
                linha.append(2)
            elif(i == 4 and j == 9):
                linha.append(6)
            elif(i == 5 and j == 4):
                linha.append(5)
            elif(i == 5 and j == 6):
                linha.append(9)
            elif(i == 6 and j == 7):
                linha.append(4)
            elif(i == 6 and j == 8):
                linha.append(1)
            elif(i == 6 and j == 9):
                linha.append(8)
            elif(i == 7 and j == 5):
                linha.append(8)
            elif(i == 7 and j == 6):
                linha.append(1)
            elif(i == 8 and j == 3):
                linha.append(2)
            elif(i == 8 and j == 8):
                linha.append(5)
            elif(i == 9 and j == 2):
                linha.append(4)
            elif(i == 9 and j == 7):
                linha.append(3)
            else:
                linha.append(randint(1,9))
        tabuleiro.append(linha)
    return tabuleiro

#nesse metodo ele avalia o atual sudoku gerando um maximo
def avaliaSolucao(solucao):
    sudokuObjetivo = retornaObjetivo()
    diferenca = 0

    for i in range(9):
        for j in range(9):
            s = solucao[i][j]
            t = sudokuObjetivo[i][j]
            diferenca += abs(s - t)
    return diferenca

#objetivo a ser alcancado
def retornaObjetivo():
    solucao =       [[2,6,4,7,1,5,8,3,9],
                    [1,3,7,8,9,2,6,4,5],
                    [5,9,8,4,3,6,2,7,1],
                    [4,2,3,1,7,8,5,9,6],
                    [8,1,6,5,4,9,7,2,3],
                    [7,5,9,6,2,3,4,1,8],
                    [3,7,5,2,8,1,9,6,4],
                    [9,8,2,3,6,4,1,5,7],
                    [6,4,1,9,5,7,3,8,2]]
    return solucao

#sao os indices que nao podem ser mudados ao rodar a funcao
#de melhor solucao
def retornaIndicesConstantes():
    indices = [(0,3),(1,0),(2,3),(2,4),(2,6),(3,8),
               (4,3),(4,5),(5,6),(5,7),(5,8),(6,4),
               (6,5),(7,2),(7,7),(8,1),(8,6)]
    return indices

#vai para um estado aleatorio e modifica para um
#valor aleatorio (nao sendo esse uma constante)
def aceitaSolucaoMelhor(solucao):
    indicesConstantes = retornaIndicesConstantes()
    i = randint(0,8)
    j = randint(0,8)
    
    if(((i,j) not in indicesConstantes)):
       solucao[i][j] = randint(1,9)
    else:
        while True:
            i = randint(0,8)
            j = randint(0,8)

            if(((i,j) not in indicesConstantes)):
                solucao[i][j] = randint(1,9)
                break









            
                
