
# toAttackCordenateValue ele é a cordenada DA PEÇA QUE VAI SER COMIDA

def isValidAttackBlackPieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if tabuleiro[x-1][y+1] == ' ':
                #direita
                result = True
            elif tabuleiro[x-1][y-1] == ' ':
                #esquerda
                result = True
        
    return result

def isValidAttackBlackPieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'B':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if tabuleiro[x+1][y+1] == ' ':
                #direita
                result = True
            elif tabuleiro[x+1][y-1] == ' ':
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToFront(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if tabuleiro[x+1][y+1] == ' ':
                #direita
                result = True
            elif tabuleiro[x+1][y-1] == ' ':
                #esquerda
                result = True
        
    return result

def isValidAttackWhitePieceToBack(x,y,tabuleiro):
    result = False

    if tabuleiro[x][y] == 'P':
        if not ((y - 1) < 0 or (y + 1) > 7): 
            if tabuleiro[x-1][y+1] == ' ':
                #direita
                result = True
            elif tabuleiro[x-1][y-1] == ' ':
                #esquerda
                result = True
        
    return result




