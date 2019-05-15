# Read the whole file as ONE STRING - UNA SOLA CADENA
# registro = fEntradas.read()

# Reads all lines at once and stores it as AN ARRAY DE STRINGS - Objeto Iterable
# line = fEntradas.readlines()

import screen2 
import config
import presentacion

def procesa(register):
    register = register.split(',')    
    numEntradas['bebe'] += int(register[0])
    numEntradas['nino'] += int(register[1])
    numEntradas['adulto'] += int(register[2])
    numEntradas['jubilado'] += int(register[3])

def main():    
    screen2.clear()
    presentacion.printScreen()
    fEntradas = open('transacciones.txt','r')
    myLine = fEntradas.readline()
    while myLine != '':
        procesa(myLine)
        myLine = fEntradas.readline()
    screen2.Print('Resumen de Ventas de Entrada Diario', line=1, column=1)
    screen2.Print('-'*50, line=2, column=1, nl=True)

    precioTotal = 0

    for key in numEntradas:

        screen2.Print(numEntradas[key],
            line=config.entradasQ[key]['cantidad'][0],
            column=config.entradasQ[key]['cantidad'][1])

        screen2.Print('${:7.2f}'.format(numEntradas[key] * config.preciosE[key]),
            line=config.entradasQ[key]['precioAcum'][0],
            column=config.entradasQ[key]['precioAcum'][1])

        precioTotal += numEntradas[key] * config.preciosE[key]
        
    
    screen2.Print('${:7.2f}'.format(precioTotal), line=9, column=19, style='bold')

    screen2.locate(11,1)

numEntradas = {
    'bebe': 0,
    'nino': 0,
    'adulto': 0,
    'jubilado': 0
}

main()
