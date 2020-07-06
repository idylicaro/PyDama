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

def hasEnemyRight(coorThisPiece, coorAction, tabuleiro, yDirection):
    enemyPiece= tabuleiro[coorAction[0]][coorAction[1]]
    if yDirection == 'UP':
        if tabuleiro[coorThisPiece[0]-1][coorThisPiece[1]+1] == enemyPiece:
            return True
    else:
        if tabuleiro[coorThisPiece[0]+1][coorThisPiece[1]+1] == enemyPiece:
            return True
    return False

def hasEnemyLeft(coorThisPiece, coorAction, tabuleiro, yDirection):
    enemyPiece= tabuleiro[coorAction[0]][coorAction[1]]
    if yDirection == 'UP':
        if tabuleiro[coorThisPiece[0]-1][coorThisPiece[1]-1] == enemyPiece:
            return True
    else:
        if tabuleiro[coorThisPiece[0]+1][coorThisPiece[1]-1] == enemyPiece:
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
            if hasEnemyRight(coorThisPiece,coorEnemy,tabuleiro,'DOWN'):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')

        else:
            coorEnemy = [coorThisPiece[0]+1,coorThisPiece[1]-1]
            if hasEnemyLeft(coorThisPiece,coorEnemy,tabuleiro,'DOWN'):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')

    else:
        if getDirectionHorizontalMoviment(coorThisPiece, coorAction) == 'RIGHT':
            coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]+1]
            if hasEnemyRight(coorThisPiece,coorEnemy,tabuleiro,'UP'):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')
        else:
            coorEnemy = [coorThisPiece[0]-1,coorThisPiece[1]-1]
            if hasEnemyLeft(coorThisPiece,coorEnemy,tabuleiro,'UP'):
                if isEmptyPosition(coorAction,tabuleiro) and isValidPosition(coorAction):
                    replacePiece(coorThisPiece,coorEnemy,coorAction,tabuleiro)
                else:
                    print('Não é possivel esse ataque!')

def isEmptyPosition(coordenate,tabuleiro):
    return tabuleiro[coordenate[0]][coordenate[1]] == ' '

def isValidPosition(coordenate):
    y =  coordenate[1]
    return not ((y - 1) < 0 or (y + 1) > 7)
