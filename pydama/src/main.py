#!python3
import view , controller
from view import presentation
from controller import gameControl
player1 = 12
player2 = 12
tabuleiro = gameControl.initializeTabuleiro()
presentation.display(tabuleiro)


