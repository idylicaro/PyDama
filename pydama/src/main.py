#!python3
import view , controller
from view import presentation
from controller import gameControl

player1Piece = 'B'
player2Piece = 'P'
player1Score = 12
player2Score = 12

#while (player1 != 0 or player2 != 0):
tabuleiro = gameControl.initializeTabuleiro()
presentation.display(tabuleiro)

print('Qual peça deseja movimentar?')
coorPlayer = gameControl.getCoordenadas()

print('Onde deseja colocar sua peça?')
coorAction = gameControl.getCoordenadas()


