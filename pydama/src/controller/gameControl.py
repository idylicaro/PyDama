def initializeTabuleiro():
    tabuleiro =[[0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
    
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            tabuleiro[i][j] = 'x'

    return tabuleiro