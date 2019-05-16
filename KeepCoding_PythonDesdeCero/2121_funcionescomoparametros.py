# Funciones de Primer Nivel
# aceptan funciones como parametros de Entrada

def normal(x):
    return x

def cuadrados(x):
    return x * x

def sumaTodos(limitTo, myfunction):
    resultado = 0
    for i in range(limitTo+1):
        resultado += myfunction(i)
    return resultado

print(sumaTodos(5, normal))
print(sumaTodos(3, cuadrados))
