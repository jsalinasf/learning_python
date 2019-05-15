def clearScreen():
    print('\033[2J')


def locateCursor(line, column):
    print('\033[{};{}H'.format(line,column),end='')

def clearLine(line=None,column=None):
    if line is not None and column is not None:
        locateCursor(line,column)
    elif line is not None:
        locateCursor(line,1)
    
    print('\033[K',end='')

def Print(cadena,line=None,column=None,delEnd=False):
    if line is not None and column is not None:
        locateCursor(line,column)
    if delEnd:
        clearLine()
    print(cadena,end='')

def Input(msg, line, column, delEnd=True):
    locateCursor(line, column)
    if delEnd:
        clearLine()
    return input(msg)

def Format(style, colorText=37, colorBackground=40):
    print('\033[{};{};{}m'.format(style,colorText,colorBackground),end='')

def Reset():
    Format(0,37,40)

