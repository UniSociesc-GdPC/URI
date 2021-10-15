#3142 - Excel Bugado
while True:
    try:
        coluna = input()

        if len(coluna) > 3:
            print("Essa coluna nao existe Tobias!")
        else:
            if (len(coluna) == 1):
                value = ord(coluna[0])-64
            if (len(coluna) == 2):
                value = ((ord(coluna[0])-64)*26)+(ord(coluna[1])-64)
            if (len(coluna) == 3):
                value = ((ord(coluna[0])-64)*676)+((ord(coluna[1])-64)*26)+(ord(coluna[2])-64)
            if(value > 16384):
                print("Essa coluna nao existe Tobias!")
            else:
                print(value)
    except EOFError:
        break