#!python3
import view , controller, os
from view import presentation
from controller import gameControl
from controller import attackControl 

turno = 0
player1Piece = 'B'
player2Piece = 'P'
player1Score = 12
player2Score = 12
currentPlayer  = ''
lastPlayerPiece = 'P'

tabuleiro = gameControl.initializeTabuleiro()
tabuleiro[2][3] = 'B' 
tabuleiro[3][4] = 'P'
tabuleiro[4][5] = ' '
tabuleiro[2][7] = ' '
tabuleiro[3][6] = 'P'

while (player1Score != 0 or player2Score != 0):
    print('::::::::::: Turno {} :::::::::::'.format(turno))
    if turno % 2 == 0:
        print('::::: Turno Peças Brancas :::::')
        currentPlayer = 'Branca'
    else:
        print('\n','::::: Turno Peças Pretas ::::: ')
        currentPlayer = 'Preta'

    presentation.display(tabuleiro)

    print('Qual peça {} deseja movimentar?'.format(currentPlayer))
    coorPlayer = gameControl.getCoordenadas()

    # Esse while ele não deixa o usuario jogar duas vezes seguidas
    while lastPlayerPiece == tabuleiro[coorPlayer[0]][coorPlayer[1]]:
        print('Selecione a peça do turno!({})'.format(currentPlayer))
        print('Qual peça {} deseja movimentar?'.format(currentPlayer))
        coorPlayer = gameControl.getCoordenadas()


    print('Onde deseja colocar sua peça?')
    coorAction = gameControl.getCoordenadas()

    QuantidadePeçaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
    while QuantidadePeçaComida != 0:
        coorPlayer = coorAction
        
        if (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]+1,coorPlayer[1]-1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]+2,coorPlayer[1]-2])
            and attackControl.isEmptyPosition([coorPlayer[0]+2,coorPlayer[1]-2],tabuleiro)):

            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]-1,coorPlayer[1]-1],tabuleiro)
             and attackControl.isValidPosition([coorPlayer[0]-2,coorPlayer[1]-2])
             and attackControl.isEmptyPosition([coorPlayer[0]-2,coorPlayer[1]-2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]+1,coorPlayer[1]+1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]+2,coorPlayer[1]+2])
            and attackControl.isEmptyPosition([coorPlayer[0]+2,coorPlayer[1]+2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]-1,coorPlayer[1]+1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]-2,coorPlayer[1]+2])
            and attackControl.isEmptyPosition([coorPlayer[0]-2,coorPlayer[1]+2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        else:
            os.system('cls')
            print("Não há mais ataque encadeado para ser realizado!")
            break
            
        QuantidadePeçaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
        

    lastPlayerPiece = tabuleiro[coorPlayer[0]][coorPlayer[1]]
    turno = turno + 1

# BRANCA PARA BAIXO DIEIRA (VERIFICADO)
# PRETA PARA CIMA ESQUERDA (VERIFICADO)
# BRANCA PARA BAIXO ESQUERDA (VERIFICADO)
# PRETA PARA CIMA direita (VERIFICADO)

def getPiece(coordenate,tabuleiro):
    return tabuleiro[coordenate[0]][coordenate[1]]