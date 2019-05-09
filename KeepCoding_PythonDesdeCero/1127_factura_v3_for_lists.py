
totalItems = 0
precioTotal = 0

precio = float(input ('Precio Unitario: '))
unidades = float(input('Numero de Items: '))

listaPrecios = []
listaUnidades = []


while (unidades > 0 and precio > 0):
    totalU = unidades * precio
    listaPrecios.append(precio)
    listaUnidades.append(unidades)

    totalItems += unidades
    precioTotal += totalU

    precio = float(input ('Precio Unitario: '))
    unidades = float(input('Numero de Items: '))

print('\n')

indice = 0
for myPrice, myUnit in zip(listaPrecios, listaUnidades):
    print('${} - {} - ${}\n'.format(round(listaPrecios[indice],2),listaUnidades[indice],round(listaPrecios[indice]*listaUnidades[indice],2)))

print('-' * 50)
print('Total: ${}'.format(round(precioTotal,2)))
print('Unidades: {}'.format(totalItems))

