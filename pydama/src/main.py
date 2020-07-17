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

    # Esse while ele não deixa o usuario selecionar a mesmo time duas vezes em rounds consecutivos
    while (lastPlayerPiece == tabuleiro[coorPlayer[0]][coorPlayer[1]]
        or (lastPlayerPiece == '$' and tabuleiro[coorPlayer[0]][coorPlayer[1]] == 'P')
        or (lastPlayerPiece == '#' and tabuleiro[coorPlayer[0]][coorPlayer[1]] == 'B')
        or (lastPlayerPiece == 'B' and tabuleiro[coorPlayer[0]][coorPlayer[1]] == '#')
        or (lastPlayerPiece == 'P' and tabuleiro[coorPlayer[0]][coorPlayer[1]] == '$')):
        print('Selecione a peça do turno!({})'.format(currentPlayer))
        print('Qual peça {} deseja movimentar?'.format(currentPlayer))
        coorPlayer = gameControl.getCoordenadas()

    # Recebe Coordenada da movimentação
    print('Onde deseja colocar sua peça?')
    coorAction = gameControl.getCoordenadas()
    
    QuantidadePecaComida = -1 #retorno do ataque 

    #Escolha de movimentação ou ataque de acordo com o tipo de jogada e peça
    moveSuccess = False
    if tabuleiro[coorPlayer[0]][coorPlayer[1]] == '$' or tabuleiro[coorPlayer[0]][coorPlayer[1]] == '#' :
        moveSuccess = damaPiece.isValidDamaMove(coorPlayer, coorAction,tabuleiro)
        if moveSuccess:
            damaPiece.cleanDiagonalIntervalAndReplace(coorPlayer,coorAction, tabuleiro)
    else:
        moveSuccess = moveControl.move(coorPlayer,coorAction,tabuleiro) 

    if not moveSuccess :
            QuantidadePecaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
            quantidadeDePecaComidaNoRound += QuantidadePecaComida

    #em caso de erro na movimentação ou ataque ele entra nesse while assim obrigando o jogador fazer uma jogada valida
    while moveSuccess == False and (QuantidadePecaComida == 0):
        presentation.display(tabuleiro)
        print('Tente um movimento valido!')
        print('Onde deseja colocar sua peça?')
        coorAction = gameControl.getCoordenadas()

        if tabuleiro[coorPlayer[0]][coorPlayer[1]] == '$' or tabuleiro[coorPlayer[0]][coorPlayer[1]] == '#' :
            moveSuccess = damaPiece.isValidDamaMove(coorPlayer, coorAction,tabuleiro)
            if moveSuccess: 
                damaPiece.cleanDiagonalIntervalAndReplace(coorPlayer,coorAction, tabuleiro)
        else: 
            moveSuccess = moveControl.move(coorPlayer,coorAction,tabuleiro)

        if not moveSuccess :
            QuantidadePecaComida = attackControl.attack(coorPlayer,coorAction,tabuleiro)
            quantidadeDePecaComidaNoRound += QuantidadePecaComida
    
    # Ataques consecutivos 
    while QuantidadePecaComida != 0 and not moveSuccess:
        coorPlayer = coorAction
        # DOWN-LEFT
        if (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]+1,coorPlayer[1]-1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]+2,coorPlayer[1]-2])
            and attackControl.isEmptyPosition([coorPlayer[0]+2,coorPlayer[1]-2],tabuleiro)):

            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        # UP-LEFT
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]-1,coorPlayer[1]-1],tabuleiro)
             and attackControl.isValidPosition([coorPlayer[0]-2,coorPlayer[1]-2])
             and attackControl.isEmptyPosition([coorPlayer[0]-2,coorPlayer[1]-2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        # Down-RIGTH
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]+1,coorPlayer[1]+1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]+2,coorPlayer[1]+2])
            and attackControl.isEmptyPosition([coorPlayer[0]+2,coorPlayer[1]+2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        # UP-RIGTH
        elif (attackControl.hasEnemy(coorPlayer,[coorPlayer[0]-1,coorPlayer[1]+1],tabuleiro)
            and attackControl.isValidPosition([coorPlayer[0]-2,coorPlayer[1]+2])
            and attackControl.isEmptyPosition([coorPlayer[0]-2,coorPlayer[1]+2],tabuleiro)):
            
            presentation.display(tabuleiro)
            print('Onde deseja colocar sua peça?')
            coorAction = gameControl.getCoordenadas()
        else:
            print()
            print("Não há mais ataque encadeado para ser realizado!")
            break
        QuantidadePecaComida = attackControl.attack(coorPlayer, coorAction,tabuleiro)
    
    # a cada round ele verifica se nenhuma peça precisa de promoção
    for i in range (0,8,7):
        for j in range(0,8):
            damaPiece.isLastField([i,j], tabuleiro)
            

    quantidadeDePecaComidaNoRound += QuantidadePecaComida
    lastPlayerPiece = 'P' if currentPlayer == 'Preta' else 'B'
    turno += 1

def getPiece(coordenate,tabuleiro):
    """ Retorna a peça na coordenada """
    return tabuleiro[coordenate[0]][coordenate[1]]