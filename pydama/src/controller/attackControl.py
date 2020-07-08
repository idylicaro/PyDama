def getDirectionVerticalMoviment(coordenateThisPiece, coordenateAction):
    if coordenateThisPiece[0] < coordenateAction[0]:
        return 'DOWN'
    else:
        return 'UP'

def getDirectionHorizontalMoviment(coordenateThisPiece, coordenateAction):
        if coordenateThisPiece[1] < coordenateAction[1]:
            return 'RIGHT'
        else:
            return 'LEFT'

def hasEnemy(coorThisPiece, coorAction, tabuleiro):
#coor action é a cordenada em si do enemy
    if isValidPosition(coorAction):
        enemyPiece= tabuleiro[coorAction[0]][coorAction[1]]
        thisPiece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]] 
        if thisPiece != enemyPiece and enemyPiece != ' ':
            return True
    return False

def replacePiece(coorThisPiece,coorEnemy,coorAfter,tabuleiro):
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = ' '
    tabuleiro[coorEnemy[0]][coorEnemy[1]] = ' '
    tabuleiro[coorAfter[0]][coorAfter[1]] = piece
    
def attack(coorThisPiece, coorAction,tabuleiro): 

    if getDirectionVerticalMoviment(coorThisPiece,coorAction) == 'DOWN':
        if getDirectionHorizontalMoviment(coorThisPiece, coorAction) == 'RIGHT':
            coorEnemy = [coorThisPiece[0]+1,coorThisPiece[1]+1]
            if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')
                    return 0

        else:
            coorEnemy = [coorThisPiece[0]+1,coorThisPiece[1]-1]
            if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')
                    return 0

    else:
        if getDirectionHorizontalMoviment(coorThisPiece, coorAction) == 'RIGHT':
            coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]+1]
            if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')
                    return 0
        else:
            coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]-1]
            if hasEnemy(coorThisPiece,coorEnemy,tabuleiro):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')
                    return 0
    return 1

def isEmptyPosition(coordenate,tabuleiro):
    return tabuleiro[coordenate[0]][coordenate[1]] == ' '

def isValidPosition(coordenate):
    x = coordenate[0]
    y = coordenate[1]
    return (y >= 0 and y <= 7) and (x >= 0 and x <= 7)
