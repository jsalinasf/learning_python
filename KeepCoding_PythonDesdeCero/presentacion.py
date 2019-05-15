import screen2

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    edad = screen2.Input('Ingresar Edad: ',line=1, column=1)
    while validaEdad(edad) == False:
        screen2.Print('Edad Invalida', line=25, colum=1, style='bold', color='yellow', back='red')
        edad = screen2.Input('Ingresar Edad: ', line=1, column=1)        
    screen2.clearLine(25)
    return int(edad)

def printScreen():
    screen2.Print('Bebe....:   -', line=4, column=5)
    screen2.Print('Nino....:   -', line=5, column=5)
    screen2.Print('Adulto..:   -', line=6, column=5)
    screen2.Print('Jubilado:   -', line=7, column=5)
    
    screen2.Format(1)
    screen2.Print('Total....:',line=9,column=8)
    screen2.Reset()