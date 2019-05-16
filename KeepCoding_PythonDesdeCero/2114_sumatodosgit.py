def sumaTodos(limitTo):
    resultados = 0
    for i in range (1,limitTo+1):
        resultados += i
    return resultados

print(sumaTodos(5))
