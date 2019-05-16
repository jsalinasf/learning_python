def sumaTodos(limitTo, myfunction):
    resultado = 0
    for i in range(limitTo+1):
        resultado += myfunction(i)
    return resultado


print(sumaTodos(3, lambda x: x**3))
print(sumaTodos(3, lambda x: x*2))

triple = lambda x: x * 3
print(sumaTodos(3, triple))


# Si necesitara enviar mas parametros a la funcion lambda
# print(sumaTodos(3, lambda x,y: x*y))
