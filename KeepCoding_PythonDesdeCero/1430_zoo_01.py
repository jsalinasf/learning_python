def calcularPrecioEntrada(e):
    if e > 0 and e < 2:
        precio = 0
    elif e < 13:
        precio = 14
    elif e < 65:
        precio = 23
    else:
        precio = 18
    return precio

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            return True
        return False
    except:
        return False


def pedirEdad():
    edad = input("Ingresar Edad: ")
    while validaEdad(edad) == False:
        print('Dato ingresado no correcto')
        edad = input("Ingresar Edad: ")
    edad = int(edad)
    return edad


edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print("Precio Entrada: {}".format(precioE))
    precioTotal += precioE
    edad = pedirEdad()

print("Total: {}".format(precioTotal))
