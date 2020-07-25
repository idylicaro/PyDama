import controller
from controller import attackControl

def isLastField(coor, tabuleiro):
    """ Verifica coordenada se é valido para a promoção da peça para dama """
    if tabuleiro[coor[0]][coor[1]] == 'B':
        if coor[0] == 7:
            replace(coor,tabuleiro)
    elif tabuleiro[coor[0]][coor[1]] == 'P':
        if coor[0] == 0:
            replace(coor,tabuleiro)
    
def replace(coorThisPiece, tabuleiro):
    """ Troca da peça para a dama """
    if tabuleiro[coorThisPiece[0]][coorThisPiece[1]] == 'B': #White
        tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = '#'
    elif tabuleiro[coorThisPiece[0]][coorThisPiece[1]] == 'P': #Black
        tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = '$'

def isValidDamaMove(coorThisPiece, coorToMove, tabuleiro):
    """ Verifica se a movimentação da dama é valida """
    thisPiece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    friend = 'B' if thisPiece == '#' else 'P'

    if isDiagonal(coorThisPiece, coorToMove):
        print('sasuahshau')
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


def cleanDiagonalIntervalAndReplace(coorThisPiece, coorToMove, tabuleiro):
    """ Faz limpa o intervalo da movimentaçao da dama e realoca a mesma """
    if (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'RIGHT'
    and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'UP'):
        i =coorThisPiece[0] - 1
        j =coorThisPiece[1] + 1
        while True:
            # Condição de parada
            if i == coorToMove[0]-1 and j == coorToMove[1]+1:
                break

            tabuleiro[i][j] = ' '
            i-=1    
            j+=1
    
    elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'RIGHT'
    and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'DOWN'):
        i =coorThisPiece[0] + 1 # LINHAS
        j =coorThisPiece[1] + 1# COLUNAS
        while True:
            # Condição de parada
            if i == coorToMove[0]+1 and j == coorToMove[1]+1:
                break
            tabuleiro[i][j] = ' '
            i+=1
            j+=1
            
    elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'Left'
    and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'UP'):
        i =coorThisPiece[0]
        j =coorThisPiece[1]
        while True:
            # Condição de parada
            if i == coorToMove[0]-1 and j == coorToMove[1]-1:
                break
            tabuleiro[i][j] = ' '
            i-=1
            j-=1
            
    elif (attackControl.getDirectionHorizontalMoviment(coorThisPiece, coorToMove) == 'Left'
    and attackControl.getDirectionVerticalMoviment(coorThisPiece, coorToMove) == 'DOWN'):
        i =coorThisPiece[0]
        j =coorThisPiece[1]
        while True:
            # Condição de parada
            if i == coorToMove[0]+1 and j == coorToMove[1]-1:
                break
            tabuleiro[i][j] = ' '
            i+=1
            j-=1
    replacePiece(coorThisPiece, coorToMove, tabuleiro)
    
                
def replacePiece(coorThisPiece, coorToMove, tabuleiro):
    """ Realoca a peça para a coordenada desejada """
    piece = tabuleiro[coorThisPiece[0]][coorThisPiece[1]]
    tabuleiro[coorThisPiece[0]][coorThisPiece[1]] = ' '
    tabuleiro[coorToMove[0]][coorToMove[1]] = piece

def isDiagonal(coorThisPiece, coorToMove):
    coorXDelta = abs(coorThisPiece[0] - coorToMove[0])
    coorYDelta = abs(coorThisPiece[1] - coorToMove[1])
    return coorXDelta != 0 and coorYDelta != 0 and coorXDelta == coorYDelta