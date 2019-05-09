
def centigrados(start, stop):
    print('°F \t °C')
    print('-' * 10)
    for grados in range (start, stop + 10, 10):        
        nuevaTemp = round((grados - 32) * 5/9,0)
        print('{}°F \t {}°C'.format(grados,nuevaTemp))

def farenheit(start, stop):
    print('°C \t °F')
    print('-' * 10)
    for grados in range (start, stop + 10, 10):        
        nuevaTemp = round(((grados * 9/5) + 32),0)
        print('{}°C \t {}°F'.format(grados,nuevaTemp))

## Main
tipo = 'C'
while tipo != 'S':
    tipo = input('\"C\" para Centigrados \"F\" para Farenheit o \"S\" para salir: ')
    tipo = tipo.upper()
    if tipo == "C":
        centigrados(0, 230)
    elif tipo == "F":
        farenheit(0, 100)
    elif tipo == "S":
        print('Bye..!')
    else:
        print('Tipo Incorrecto')