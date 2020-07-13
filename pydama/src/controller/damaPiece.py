import controller
from controller import attackControl

def isLastField(coor, tabuleiro):
    if tabuleiro[coor[0]][coor[1]] == 'B':
        if coor[0] == 7:
            replace(coor,tabuleiro)
    elif tabuleiro[coor[0]][coor[1]] == 'P':
        if coor[0] == 0:
            replace(coor,tabuleiro)
    

def replace(coorThisPiece, tabuleiro):
    if tabuleiro[coorThisPiece[0]][coorThisPiece[1]] == 'B': #White
        tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = '#'
    elif tabuleiro[coorThisPiece[0]][coorThisPiece[1]] == 'P': #Black
        tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = '$'

def moveDama(coorThisPiece, coorToMove, tabuleiro):
    thisPiece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    friend = 'B' if thisPiece == '#' else 'P'

    if coorThisPiece[0] - coorToMove[0] != 0 and coorThisPiece[1] - coorToMove[1] != 0:

        if (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'RIGHT'
        and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'UP'):
            i =coorThisPiece[0] - 1
            j =coorThisPiece[1] + 1
            while True:
                # Condição de parada
                if i == coorToMove[0]-1 and j == coorToMove[1]+1:
                    break
                # Field is empty
                if(attackControl.isEmptyPosition([i,j],tabuleiro)):
                    i-=1
                    j+=1
                    continue

                # return false if has friend
                if(tabuleiro[i-1][j+1] == friend):
                    return False
                # has enemy and next field is empty
                if(tabuleiro[i][j] != thisPiece and tabuleiro[i][j] != ' ' and tabuleiro[i][j] != friend):
                    if(tabuleiro[i-1][j+1] == ' '):
                        i-=1
                        j+=1
                        continue
                    else:
                        return False
        
        elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'RIGHT'
        and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'DOWN'):
            i =coorThisPiece[0] + 1 # LINHAS
            j =coorThisPiece[1] + 1# COLUNAS
            while True:
                
                # Condição de parada
                if i == coorToMove[0]+1 and j == coorToMove[1]+1:
                    break
                # Field is empty
                if(attackControl.isEmptyPosition([i,j],tabuleiro)):
                    i+=1
                    j+=1
                    continue

                # return false if has friend
                if(tabuleiro[i+1][j+1] == friend):
                    return False
                # has enemy and next field is empty
                if(tabuleiro[i][j] != thisPiece and tabuleiro[i][j] != ' ' and tabuleiro[i][j] != friend):
                    if(tabuleiro[i+1][j+1] == ' '):
                        i+=1
                        j+=1
                        continue
                    else:
                        return False
                
        elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'Left'
        and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'UP'):
            i =coorThisPiece[0]
            j =coorThisPiece[1]
            while True:
                # Condição de parada
                if i == coorToMove[0]-1 and j == coorToMove[1]-1:
                    break
                # Field is empty
                if(attackControl.isEmptyPosition([i,j],tabuleiro)):
                    i-=1
                    j-=1
                    continue

                # return false if has friend
                if(tabuleiro[i-1][j-1] == friend):
                    return False
                # has enemy and next field is empty
                if(tabuleiro[i][j] != thisPiece and tabuleiro[i][j] != ' ' and tabuleiro[i][j] != friend):
                    if(tabuleiro[i-1][j-1] == ' '):
                        i-=1
                        j-=1
                        continue
                    else:
                        return False

        elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'Left'
        and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'DOWN'):
            i =coorThisPiece[0]
            j =coorThisPiece[1]
            while True:
                i+=1
                j-=1
                # Condição de parada
                if i == coorToMove[0]+1 and j == coorToMove[1]-1:
                    break
                # Field is empty
                if(attackControl.isEmptyPosition([i,j],tabuleiro)):
                    i+=1
                    j-=1
                    continue

                # return false if has friend
                if(tabuleiro[i+1][j-1] == friend):
                    return False
                # has enemy and next field is empty
                if(tabuleiro[i][j] != thisPiece and tabuleiro[i][j] != ' ' and tabuleiro[i][j] != friend):
                    if(tabuleiro[i+1][j-1] == ' '):
                        i+=1
                        j-=1
                        continue
                    else:
                        return False
        
    return True
