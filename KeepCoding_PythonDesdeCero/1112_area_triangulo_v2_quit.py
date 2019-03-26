def isFloat(num):
    try:
        float(num)
        return True
    except:
        return False

B = input('Base del Triangulo: ')

if isFloat(B):
    b = float(B)
else:
    print(B, 'Debe ser un numero')
    quit()

H = input('Altura del Triangulo: ')

if isFloat(H):
    h = float(H)
else:
    print(H, 'Debe ser un numero')
    quit()


area = (b * h)/2

print('Superficie del Triangulo: ', round(area, 2))