# xy ele é a cordenada DA PEÇA QUE VAI SER COMIDA
import gameControl

def isValidAttackBlackPieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightFrontValidEat(x,y,tabuleiro):
                #direita
                result = True
            elif isLeftFrontValidEat(x,y,tabuleiro):
                #esquerda
                result = True
        
    return result

def isValidAttackBlackPieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightBackValidEat(x,y,tabuleiro):
                #direita
                result = True
            elif isLeftBackValidEat(x,y,tabuleiro):
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightBackValidEat(x,y,tabuleiro):
                #direita
                result = True
            elif isLeftBackValidEat(x,y,tabuleiro):
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if isRightFrontValidEat(x,y,tabuleiro):
                #direita
                result = True
            elif isLeftFrontValidEat(x,y,tabuleiro):
                #esquerda
                result = True
        
    return result

def isLeftFrontValidEat(x,y,tabuleiro):
    if tabuleiro[x-1][y-1] == ' ':
        return True
    else:
        return False

def isLeftBackValidEat(x,y,tabuleiro):
    if tabuleiro[x+1][y-1] == ' ':
        return True
    else:
        return False

def isRightFrontValidEat(x,y,tabuleiro):
    if tabuleiro[x-1][y+1] == ' ':
        return True
    else:
        return False

def isRightBackValidEat(x,y,tabuleiro):
    if tabuleiro[x+1][y+1] == ' ':
        return True
    else:
        return False

def isBlack(coorPiece, tabuleiro):
    if tabuleiro[coorPiece[0]][coorPiece[1]] == 'P':
        return True
    return False

def isWhite(coorPiece, tabuleiro):
    if tabuleiro[coorPiece[0]][coorPiece[1]] == 'B':
        return True
    return False

def attackMove(coordenateThisPiece, coordenateEnemyPiece, tabuleiro, directionY):
    piece = tabuleiro[coordenateThisPiece[0]][coordenateThisPiece[1]]
    tabuleiro[coordenateThisPiece[0]][coordenateThisPiece[1]] = ' '
    tabuleiro[coordenateEnemyPiece[0]][coordenateEnemyPiece[1]] = ' '
    
    if directionY == 'UP':
        if isLeftFrontValidEat():
            tabuleiro[coordenateEnemyPiece[0]-1][coordenateEnemyPiece[1]-1] = piece
        elif isRightFrontValidEat():
            tabuleiro[coordenateEnemyPiece[0]-1][coordenateEnemyPiece[1]+1] = piece
    elif directionY == 'DOWN':
        if isLeftBackValidEat():
            tabuleiro[coordenateEnemyPiece[0]+1][coordenateEnemyPiece[1]-1] = piece
        elif isRightBackValidEat():
            tabuleiro[coordenateEnemyPiece[0]+1][coordenateEnemyPiece[1]+1] = piece


def attack(coordenateThisPiece, coordenateEnemyPiece, tabuleiro):
    if isBlack(coordenateThisPiece,tabuleiro):
        if isValidAttackBlackPieceToBack(coordenateEnemyPiece[0], coordenateEnemyPiece[1], tabuleiro):
            attackMove(coordenateThisPiece, coordenateEnemyPiece, tabuleiro, 'DOWN')
        elif isValidAttackBlackPieceToFront(coordenateEnemyPiece[0], coordenateEnemyPiece[1], tabuleiro):
            attackMove(coordenateThisPiece, coordenateEnemyPiece, tabuleiro, 'UP')

    elif isWhite(coordenateThisPiece,tabuleiro):
        if isValidAttackWhitePieceToBack(coordenateEnemyPiece[0], coordenateEnemyPiece[1], tabuleiro):
            attackMove(coordenateThisPiece, coordenateEnemyPiece, tabuleiro, 'UP')
        elif isValidAttackWhitePieceToFront(coordenateEnemyPiece[0], coordenateEnemyPiece[1], tabuleiro):
            attackMove(coordenateThisPiece, coordenateEnemyPiece, tabuleiro, 'DOWN')

