def clearScreen():
    print('\033[2J')


def locateCursor(line, column):
    print('\033[{};{}H'.format(line,column),end='')

def clearLine():
    print('\033[K',end='')

def Print(cadena,line,column,delEnd=False):
    locateCursor(line,column)
    if delEnd:
        clearLine()
    print(cadena,end='')

def Input(msg, line, column, delEnd=True):
    locateCursor(line, column)
    if delEnd:
        clearLine()
    return input(msg)
