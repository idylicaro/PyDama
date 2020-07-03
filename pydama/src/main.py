#!python3
import view , controller
from view import presentation
from controller import gameControl

tabuleiro = gameControl.initializeTabuleiro()
presentation.display(tabuleiro)


