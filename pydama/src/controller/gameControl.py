import os

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
            tabuleiro[i][j] = ' '

    initializePlayerColorBlack(tabuleiro)
    initializePlayerColorWhite(tabuleiro)
    return tabuleiro

def initializePlayerColorBlack(tabuleiro):
    for i in range(7,4,-1):  
        for j in range(0,8):
            if i % 2!=0:
                if(j % 2 == 0):
                    tabuleiro[i][j] = 'P'
                else:
                    tabuleiro[i][j] = ' '
            else:
                if(j % 2 != 0):
                    tabuleiro[i][j] = 'P'
                else:
                    tabuleiro[i][j] = ' '
        
def initializePlayerColorWhite(tabuleiro):
    for i in range(0,3):  
        for j in range(0,8):
            if i % 2!=0:
                if(j % 2 == 0):
                    tabuleiro[i][j] = 'B'
                else:
                    tabuleiro[i][j] = ' '
            else:
                if(j % 2 != 0):
                    tabuleiro[i][j] = 'B'
                else:
                    tabuleiro[i][j] = ' '
        


def convertCharCoordenateToNumber(caracter):
    if(caracter == 'A'):
        return 0
    elif(caracter == 'B'):
        return 1
    elif(caracter == 'C'):
        return 2
    elif(caracter == 'D'):
        return 3
    elif(caracter == 'E'):
        return 4
    elif(caracter == 'F'):
        return 5
    elif(caracter == 'G'):
        return 6
    elif(caracter == 'H'):
        return 7
    else:
        return -1

def isValidCharInput(inputChar):
    if(ord(inputChar)>=65 and ord(inputChar)<=72 ):
        return True
    else:
        return False

def isValidNumberInput(inputNumber):
    if inputNumber>=0 and inputNumber<=7:
        return True
    else:
        return False

def getCoordenadas():
    coordenadas = [-1,-1]
    boolIsValidChar = False
    boolIsValidNumber = False
    
    x = input("Digite a linha(A-H): ").upper()
    boolIsValidChar = isValidCharInput(x)

    while not boolIsValidChar:
        os.system('cls') #limpar cmd
        print("Digite Corretamente:")
        x = input("Digite a linha(A-H):").upper()
        boolIsValidChar = isValidCharInput(x)

    x = convertCharCoordenateToNumber(x)

    y = int(input("Digite a coluna(0-7): "))
    boolIsValidNumber = isValidNumberInput(y)

    while not boolIsValidNumber:
        #os.system('cls') #limpar cmd
        print("Digite Corretamente:")
        y = int(input("Digite a coluna(0-7): "))
        boolIsValidNumber = isValidNumberInput(y)

    print() #pulando linha

    coordenadas[0] = x
    coordenadas[1] = y

    return coordenadas
