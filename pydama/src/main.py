#!python3
import view
from view import presentation
import controller
from controller import gameControl
from controller import attackControl 
from controller import moveControl
from controller import damaPiece

turno = 0
player1Piece = 'B'
player2Piece = 'P'
player1Score = 12
player2Score = 12
currentPlayer  = ''
lastPlayerPiece = 'P'
quantidadeDePecaComidaNoRound = 0 

tabuleiro = gameControl.initializeTabuleiro()

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
