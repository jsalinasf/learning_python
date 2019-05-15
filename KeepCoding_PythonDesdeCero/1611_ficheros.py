import screen2
import presentacion
from config import preciosE, entradasQ

numEntradas = {
    'bebe': 0,
    'nino': 0,
    'adulto': 0,
    'jubilado': 0
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

def main():
    screen2.clear()
    presentacion.printScreen()
    edad = presentacion.pedirEdad()
    precioTotal = 0

    while edad != 0:
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        numEntradas[tipoE] += 1

        screen2.Print(numEntradas[tipoE],
                        line=entradasQ[tipoE]['cantidad'][0],
                        column=entradasQ[tipoE]['cantidad'][1])

        screen2.Print('${:7.2f}'.format(numEntradas[tipoE]*precioE),
                        line=entradasQ[tipoE]['precioAcum'][0],
                        column=entradasQ[tipoE]['precioAcum'][1])

        precioTotal += precioE
        screen2.Print('${:7.2f}'.format(precioTotal), line=9, column=19, style='bold')
        edad = presentacion.pedirEdad()
    
    # Save File
    fEntradas = open('transacciones.txt','a+')
    transaccion = '{},{},{},{}\n'.format(numEntradas['bebe'],numEntradas['nino'],numEntradas['adulto'],numEntradas['jubilado'])
    fEntradas.write(transaccion)
    fEntradas.close()
    screen2.locate(11,1)

main()
