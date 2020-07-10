from controller import attackControl, gameControl

def move(coorThisPiece, coorToMove, tabuleiro):
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    print("moises cabra macho")
    if isValidMove(coorThisPiece,coorToMove,tabuleiro):
        replaceMove(coorThisPiece, coorToMove, tabuleiro)
    
    # [4,2] para [5,1]
    # se ta vazio  (V)
    # se a quantidade de casas que ele ta andando é um (V) 
    # se ta em diagonal 
    # se o movimento é valido (V)

def replaceMove(coorThisPiece, coorToMove, tabuleiro):
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = ''
    tabuleiro[coorToMove[0]][coorToMove[1]] = piece


def isValidAmountMove(coorThisPiece, coorToMove):
    """ Return true if Amount to move coordenate is one """
    return coorThisPiece[0] - coorToMove[0] == 1 or coorThisPiece[0] - coorToMove[0] == -1 

def isDiagonal(coorThisPiece,coorToMove):
    x = coorThisPiece[0] - coorToMove[0] == 1 or coorThisPiece[0] - coorToMove[0] == -1
    y = coorThisPiece[1] - coorToMove[1] == 1 or coorThisPiece[1] - coorToMove[1] == -1
    return 

def isValidMove(coorThisPiece,coorToMove,tabuleiro):
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    if piece == 'P':
        if attackControl.isEmptyPosition(coorToMove,tabuleiro):
            if isValidAmountMove(coorThisPiece,coorToMove):
                if coorThisPiece[0] > coorToMove[0]: # if go to front 
                    if isDiagonal(coorThisPiece,coorToMove):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        if attackControl.isEmptyPosition(coorToMove,tabuleiro):
            if isValidAmountMove(coorThisPiece,coorToMove):
                if coorThisPiece[0] < coorToMove[0]: # if go to front 
                    if isDiagonal(coorThisPiece,coorToMove):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

