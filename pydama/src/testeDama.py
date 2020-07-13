#!python3
import view , controller, os
from view import presentation
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
tabuleiro[0][1] = ' ' 
tabuleiro[1][0] = '$'
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
    
    # Recebe Coordenada da peça que deseja movimentar
    print('Qual peça {} deseja movimentar?'.format(currentPlayer))
    coorPlayer = gameControl.getCoordenadas()

    # Verifica se é realmente alguma peça
    isBlankPiece = True if tabuleiro[coorPlayer[0]][coorPlayer[1]] == ' ' else False
    while isBlankPiece:
        print('Qual peça {} deseja movimentar?'.format(currentPlayer))
        coorPlayer = gameControl.getCoordenadas()
        isBlankPiece = True if tabuleiro[coorPlayer[0]][coorPlayer[1]] == ' ' else False

    # Esse while ele não deixa o usuario jogar duas vezes seguidas
    while lastPlayerPiece == tabuleiro[coorPlayer[0]][coorPlayer[1]]:
        print('Selecione a peça do turno!({})'.format(currentPlayer))
        print('Qual peça {} deseja movimentar?'.format(currentPlayer))
        coorPlayer = gameControl.getCoordenadas()

    # Recebe Coordenada da movimentação
    print('Onde deseja colocar sua peça?')
    coorAction = gameControl.getCoordenadas()
    
    QuantidadePecaComida = -1 #retorno do ataque

    print('Entrou Aqui')
    if tabuleiro[coorPlayer[0]][coorPlayer[1]] == '$':
        print(damaPiece.moveDama(coorPlayer, coorAction,tabuleiro))

    moveSuccess = moveControl.move(coorPlayer,coorAction,tabuleiro) 
    if not moveSuccess :
            QuantidadePecaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
            quantidadeDePecaComidaNoRound += QuantidadePecaComida
            # moveSuccess = moveDama()
    
    while moveSuccess == False and (QuantidadePecaComida == 0):
        presentation.display(tabuleiro)
        print('Tente um movimento valido!')
        print('Onde deseja colocar sua peça?')
        coorAction = gameControl.getCoordenadas()
        moveSuccess = moveControl.move(coorPlayer,coorAction,tabuleiro)
        if not moveSuccess :
            QuantidadePecaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
            quantidadeDePecaComidaNoRound += QuantidadePecaComida
    
    while QuantidadePecaComida != 0 and not moveSuccess:
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
            #os.system('cls')
            print()
            print("Não há mais ataque encadeado para ser realizado!")
            break
        QuantidadePecaComida = attackControl.attack(coorPlayer, coorAction,tabuleiro)
    
    for i in range (0,8,7):
        for j in range(0,8):
            damaPiece.isLastField([i,j], tabuleiro)
            

    quantidadeDePecaComidaNoRound += QuantidadePecaComida
    lastPlayerPiece = 'P' if currentPlayer == 'Preta' else 'B'
    turno += 1

def getPiece(coordenate,tabuleiro):
    return tabuleiro[coordenate[0]][coordenate[1]]