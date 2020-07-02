tabuleiro = [[0,0,0,0,0,0,0,0], 
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


for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
        print(tabuleiro[i][j], end=' ')
    print()
