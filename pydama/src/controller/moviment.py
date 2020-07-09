import os
import gameControl

def movimentPecaPreta(xorigem, yorigem, xlinha, ylinha, tabuleiro):
    gameControl.getCoordenadas()
    if tabuleiro[xorigem][yorigem] == 'P':
        tabuleiro[xorigem][yorigem] = ' '
        tabuleiro[xlinha][yorigem] = 'p'
       
