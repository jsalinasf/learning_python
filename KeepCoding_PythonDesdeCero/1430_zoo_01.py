import screen

preciosE = {
    # Precios de las entradas segun su tipo
    'bebe': 0.0,
    'nino': 14.0,
    'adulto': 23.0,
    'jubilado': 18.0
}

numEntradas = {
    'bebe': 0,
    'nino': 0,
    'adulto': 0,
    'jubilado': 0
}

entradasQ = {
    # Coordenadas donde apareceran las cantidades del precio de cada entrada y el subtotal correspondiente
    # para cada tipo
    'bebe': {
        'cantidad': (4,15),
        'precioAcum': (4,19)
    },
    'nino': {
        'cantidad': (5,15),
        'precioAcum': (5,19)
    },
    'adulto': {
        'cantidad': (6,15),
        'precioAcum': (6,19)
    },
    'jubilado': {
        'cantidad': (7,15),
        'precioAcum': (7,19)
    }
}

def tipoEntrada(e):
    if e > 0 and e < 2:
        tipo = 'bebe'
    elif e < 13:
        tipo = 'nino'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    return tipo

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False

def pedirEdad():
    edad = screen.Input('Ingresar Edad: ',1,1)
    while validaEdad(edad) == False:
        screen.Print('Edad Invalida',25,1)
        edad = screen.Input('Ingresar Edad: ',1,1)        
    return int(edad)

def printScreen():
    screen.Print('Bebe....:   -',4,5)
    screen.Print('Nino....:   -',5,5)
    screen.Print('Adulto..:   -',6,5)
    screen.Print('Jubilado:   -',7,5)
    screen.Print('Total....:',9,8)

# __main__
screen.clearScreen()
printScreen()
edad = pedirEdad()
precioTotal = 0

while edad != 0:
    tipoE = tipoEntrada(edad)
    precioE = preciosE[tipoE]
    numEntradas[tipoE] += 1
    screen.locateCursor(entradasQ[tipoE]['cantidad'][0], entradasQ[tipoE]['cantidad'][1])
    print(numEntradas[tipoE])
    screen.locateCursor(entradasQ[tipoE]['precioAcum'][0], entradasQ[tipoE]['precioAcum'][1])
    # 7 viene de... 4 caracteres para la parte entera, 1 carater para la cola y 2 caracteres para decimales
    print('${:7.2f}'.format(precioE * numEntradas[tipoE]))
    precioTotal += precioE
    screen.locateCursor(9,19)
    print('${:7.2f}'.format(precioTotal))
    edad = pedirEdad()

screen.locateCursor(11,1)