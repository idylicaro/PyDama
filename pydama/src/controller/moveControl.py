from controller import attackControl, gameControl

def move(coorThisPiece, coorToMove, tabuleiro):
    """ retorna true caso seja movimentação valida, apos a validação realiza a movimentação """
    if isValidMove(coorThisPiece,coorToMove,tabuleiro):
        replaceMove(coorThisPiece, coorToMove, tabuleiro)
        return True
    return False

def replaceMove(coorThisPiece, coorToMove, tabuleiro):
    """ Realoca a peça para coordenada desejada """
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = ' '
    tabuleiro[coorToMove[0]][coorToMove[1]] = piece


def isValidAmountMove(coorThisPiece, coorToMove):
    """ Return true if Amount to move coordenate is one """
    return coorThisPiece[0] - coorToMove[0] == 1 or coorThisPiece[0] - coorToMove[0] == -1 

def isDiagonal(coorThisPiece,coorToMove):
    """ verifica se a movimentação é diagonal """
    x = coorThisPiece[0] - coorToMove[0] == 1 or coorThisPiece[0] - coorToMove[0] == -1
    y = coorThisPiece[1] - coorToMove[1] == 1 or coorThisPiece[1] - coorToMove[1] == -1
    return x and y

def isValidMove(coorThisPiece,coorToMove,tabuleiro):
    """ Verifica se a movimentação é valida """
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    if piece == 'P':
        if attackControl.isEmptyPosition(coorToMove,tabuleiro):
            if isValidAmountMove(coorThisPiece,coorToMove):
                if coorThisPiece[0] > coorToMove[0]: # if go to front
                    if isDiagonal(coorThisPiece,coorToMove):
                        return True
                    
    else:
        if attackControl.isEmptyPosition(coorToMove,tabuleiro):
            if isValidAmountMove(coorThisPiece,coorToMove):
                if coorThisPiece[0] < coorToMove[0]: # if go to front
                    if isDiagonal(coorThisPiece,coorToMove):
                        return True
    
    return False


