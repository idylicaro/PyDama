#!python3
import view , controller
from view import presentation
from controller import gameControl
player1 = 12
player2 = 12
while (player1 != 0 or player2 != 0):
    tabuleiro = gameControl.initializeTabuleiro()
    presentation.display(tabuleiro)

print('ikaruz teste')


