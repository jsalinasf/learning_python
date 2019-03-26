
totalItems = 0
precioTotal = 0

precio = float(input ('Precio Unitario: '))
unidades = float(input('Numero de Items: '))


cadenaAImprimir = 'Precio - Unidades - SubTotal\n'

while (unidades > 0 and precio > 0):
    totalU = unidades * precio
    cadenaAImprimir += '${} - {} - ${}\n'.format(round(precio,2),unidades,round(totalU,2))

    totalItems += unidades
    precioTotal += totalU

    precio = float(input ('Precio Unitario: '))
    unidades = float(input('Numero de Items: '))

print('\n')
print(cadenaAImprimir)
print('-' * 50)
print('Total: ${}'.format(round(precioTotal,2)))
print('Unidades: {}'.format(totalItems))

