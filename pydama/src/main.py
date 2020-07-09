#!python3
import view , controller
from view import presentation
from controller import gameControl
player1 = 12
player2 = 12
#while (player1 != 0 or player2 != 0):
tabuleiro = gameControl.initializeTabuleiro()
presentation.display(tabuleiro)

print('Qual que movimentar')
gameControl.getCoordenadas()
'''
y = qual casa vc quer mover ou ataca

se a casa e vc ta movendo é vazia:
    move()
else:
    if a peça é preta?
        ATAQUEPRETA()
    ELSE:
        ataqueBranca()
'''