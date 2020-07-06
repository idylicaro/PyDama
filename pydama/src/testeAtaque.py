#!python3
import view , controller, os
from view import presentation
from controller import gameControl
from controller import attackControl 

player1 = 12
player2 = 12

tabuleiro = gameControl.initializeTabuleiro()
tabuleiro[2][3] = 'B' 
tabuleiro[3][4] = 'P'
tabuleiro[4][5] = ' '

while (player1 != 0 or player2 != 0):

    presentation.display(tabuleiro)

    print('Qual peça deseja movimentar?')
    coorPlayer = gameControl.getCoordenadas()

    print('Onde deseja colocar sua peça?')
    coorAction = gameControl.getCoordenadas()

    attackControl.attack(coorPlayer,coorAction,tabuleiro) 

# BRANCA PARA BAIXO DIEIRA (VERIFICADO)
# PRETA PARA CIMA ESQUERDA (VERIFICADO)
# BRANCA PARA BAIXO ESQUERDA (VERIFICADO)
# PRETA PARA CIMA direita (VERIFICADO)