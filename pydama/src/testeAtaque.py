#!python3
import view , controller
from view import presentation
from controller import gameControl

player1 = 12
player2 = 12

#while (player1 != 0 or player2 != 0):
#tabuleiro = gameControl.initializeTabuleiro()

tabuleiro =     [[0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,'B',0,0,0,0,0], 
                [0,'P',0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]

presentation.display(tabuleiro)

print('Qual peça deseja movimentar?')
coorPlayer = gameControl.getCoordenadas()

print('Onde deseja colocar sua peça?')
coorAction = gameControl.getCoordenadas()


