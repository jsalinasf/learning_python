
totalItems = 0
precioTotal = 0

precio = float(input ('Precio Unitario: '))
unidades = float(input('Numero de Items: '))

listalineasFact = []

while (unidades > 0 and precio > 0):
    totalU = unidades * precio
    item = dict()
    item['unidades'] = unidades
    item['precio'] = precio
    listalineasFact.append(item)

    totalItems += unidades
    precioTotal += totalU

    precio = float(input ('Precio Unitario: '))
    unidades = float(input('Numero de Items: '))

print('\n')

indice = 0
for item in listalineasFact:
    precioTotalItem = round(item['unidades'] * item['precio'],2)
    print('{} - ${} - ${}\n'.format(item['unidades'],round(item['precio'],2),precioTotalItem))

# item.get('UnidadesEcuador') == None --- Me sirve para validar si existe o no la clave
# sin que tire error

print('-' * 50)
print('Total: ${}'.format(round(precioTotal,2)))
print('Unidades: {}'.format(totalItems))

