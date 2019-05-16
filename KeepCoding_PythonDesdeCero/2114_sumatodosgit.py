def sumaTodos(limitTo):
    resultados = 0
    for i in range (1,limitTo+1):
        resultados += i
    return resultados

def sumaTodosLosCuadrados(limitTo):
    resultados = 0
    for i in range (1,limitTo+1):
        resultados += i * i
    return resultados

print(sumaTodos(5))
print(sumaTodosLosCuadrados(3))
