
def display (tabuleiro):
    charCodeInitial = 65 #code asc2 

    print()
    print(' ','','0','1','2','3','4','5','6','7')
    print()
    for i in range(len(tabuleiro)):  
        for j in range(len(tabuleiro[i])):
            if (j==0):
                print(chr(charCodeInitial),end='  ')
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
        charCodeInitial += 1
    print()
    print()

def coloredWhite(string):
    return '\x1b[0;30;47m' + string + '\x1b[0m'