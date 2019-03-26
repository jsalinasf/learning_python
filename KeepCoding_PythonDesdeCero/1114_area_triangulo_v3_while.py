def isFloat(num):
    try:
        float(num)
        return True
    except:
        return False

B = input('Base del Triangulo: ')
while not (isFloat(B)):
    print(B, 'Debe ser un numero')
    B = input('Base del Triangulo: ')
b = float(B)

H = input('Altura del Triangulo: ')
while not (isFloat(H)):
    print(H, 'Debe ser un numero')
    H = input('Altura del Triangulo: ')
h = float(H)

area = (b * h)/2

print('Superficie del Triangulo: ', round(area, 2))