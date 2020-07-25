def getDirectionVerticalMoviment(coordenateThisPiece, coordenateAction):
    """ Retorna a direção Vertical da movimentação """
    if coordenateThisPiece[0] < coordenateAction[0]:
        return 'DOWN'    
    return 'UP'

def getDirectionHorizontalMoviment(coordenateThisPiece, coordenateAction):
    """ Retorna a direção Horizontal da movimentação """
    if coordenateThisPiece[1] < coordenateAction[1]:
        return 'RIGHT'    
    return 'LEFT'

def hasEnemy(coorThisPiece, coorAction, tabuleiro):
    """ Verifica se há um inimigo no tabuleiro na coordenada """
    if isValidPosition(coorAction):
        enemyPiece= tabuleiro[coorAction[0]][coorAction[1]]
        thisPiece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]] 
        if thisPiece != enemyPiece and enemyPiece != ' ':
            return True
    return False

def isEmptyPosition(coordenate,tabuleiro):
    """ Verifica se é uma casa vazia """
    return tabuleiro[coordenate[0]][coordenate[1]] == ' '

def isValidPosition(coordenate):
    """ Verifica se é uma casa valida dentro do tabuleiro """
    x = coordenate[0]
    y = coordenate[1]
    return (y >= 0 and y <= 7) and (x >= 0 and x <= 7)

def isDiagonal(coorThisPiece,coorAction):
    deltaCoorX = abs(coorThisPiece[0] - coorAction[0])
    deltaCoorY = abs(coorThisPiece[1] - coorAction[1])
    return deltaCoorX != 0 and deltaCoorY != 0 and deltaCoorX == deltaCoorY

def replacePiece(coorThisPiece,coorEnemy,coorAfter,tabuleiro):
    """ Realoca a peça atual para a coordenada da movimentação """
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = ' '
    tabuleiro[coorEnemy[0]][coorEnemy[1]] = ' '
    tabuleiro[coorAfter[0]][coorAfter[1]] = piece
    
def attack(coorThisPiece, coorAction,tabuleiro): 
    """ Retorna 0 caso o ataque seja invalido, retorna 1 caso seja valido e tambem faz a realocação da peça """
    if isDiagonal(coorThisPiece,coorAction):
        if getDirectionVerticalMoviment(coorThisPiece,coorAction) == 'DOWN':
            if getDirectionHorizontalMoviment(coorThisPiece, coorAction) == 'RIGHT':
                coorEnemy = [coorThisPiece[0]+1,coorThisPiece[1]+1]
                if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                    if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                        replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)    
                        return 1
            else:
                coorEnemy = [coorThisPiece[0]+1,coorThisPiece[1]-1]
                if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                    if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                        replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                        return 1
        else:
            if getDirectionHorizontalMoviment(coorThisPiece, coorAction) == 'RIGHT':
                coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]+1]
                if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                    if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                        replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                        return 1
            else:
                coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]-1]
                if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                    if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                        replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                        return 1
    print('Não é possivel esse ataque!')
    return 0