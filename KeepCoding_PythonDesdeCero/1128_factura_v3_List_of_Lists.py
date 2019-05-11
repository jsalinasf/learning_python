
totalItems = 0
precioTotal = 0

precio = float(input ('Precio Unitario: '))
unidades = float(input('Numero de Items: '))

listalineasFact = []

while (unidades > 0 and precio > 0):
    totalU = unidades * precio
    item = []
    item.append(unidades)
    item.append(precio)
    listalineasFact.append(item)

    totalItems += unidades
    precioTotal += totalU

    precio = float(input ('Precio Unitario: '))
    unidades = float(input('Numero de Items: '))

print('\n')

indice = 0
for item in listalineasFact:
    precioTotalItem = round(item[0] * item[1],2)
    print('{:2} - ${:7.2f} - ${:7.2f}\n'.format(item[0],round(item[1],2),precioTotalItem))

print('-' * 50)
print('Total: ${:7.2f}'.format(round(precioTotal,2)))
print('Unidades: {}'.format(totalItems))

