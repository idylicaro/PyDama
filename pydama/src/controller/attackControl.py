
# toAttackCordenateValue ele é a cordenada DA PEÇA QUE VAI SER COMIDA

def isValidAttackBlackPieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightFront():
                #direita
                result = True
            elif isLeftFront():
                #esquerda
                result = True
        
    return result

def isValidAttackBlackPieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightBack():
                #direita
                result = True
            elif isLeftBack():
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightBack():
                #direita
                result = True
            elif isLeftBack():
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightFront():
                #direita
                result = True
            elif isLeftFront():
                #esquerda
                result = True
        
    return result

def isLeftFront(x,y,tabuleiro):
    if tabuleiro[x-1][y-1] == ' ':
        return True
    else:
        return False

def isLeftBack(x,y,tabuleiro):
    if tabuleiro[x+1][y-1] == ' ':
        return True
    else:
        return False

def isRightFront(x,y,tabuleiro):
    if tabuleiro[x-1][y+1] == ' ':
        return True
    else:
        return False

def isRightBack(x,y,tabuleiro):
    if tabuleiro[x+1][y+1] == ' ':
        return True
    else:
        return False


def attack(coordenateThisPiece, coordenateEnemyPiece, tabuleiro):
    return 'NADA AINDA';
