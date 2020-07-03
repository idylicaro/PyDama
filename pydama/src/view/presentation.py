
whiteColor = ''

def display (tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (i % 2!=0):
                if(j % 2 == 0):
                    print(tabuleiro[i][j], end=' ')
                else:
                    print(coloredWhite(tabuleiro[i][j]), end=' ')
            else:
                if(j % 2 != 0):
                    print(tabuleiro[i][j], end=' ')
                else:
                    print(coloredWhite(tabuleiro[i][j]), end=' ')
        print()

def coloredWhite(string):
    return '\x1b[0;30;47m' + string + '\x1b[0m'