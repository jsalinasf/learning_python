# Una funcion es de nivel superior si:
#   Recibe una funcion como parametro o
#   Retorna una funcion como resultado de la funcion o
#   Todas las anteriores

def myMax(*l):
    if len(l) == 0:
        return 0
    maxValue = l[0]
    for ix in range(1, len(l)):
        if l[ix] > maxValue:
            maxValue = l[ix]
    return maxValue

def myMin(*l):
    if len(l) == 0:
        return 0
    minValue = l[0]
    for ix in range(1, len(l)):
        if l[ix] < minValue:
            minValue = l[ix]
    return minValue

def myAverage(*l):
    if len(l) == 0:
        return 0
    totalSum = 0
    for ix in range(len(l)):
        totalSum += l[ix]
    return totalSum / len(l)

funciones = {
    'maximo': myMax,
    'minimo': myMin,
    'promedio': myAverage
}

def returnFunction(nombre):
    nombre = nombre.lower()
    if funciones.get(nombre):
        return funciones[nombre]
    
    return None

print(returnFunction('maximo')(1,3,5,997,-1))
print(returnFunction('minimo')(1,3,5,997,-1))
print(returnFunction('promedio')(1,3,5,997,-1))

varMax = returnFunction('maximo')
print(varMax(1,3,5,997,-1))
varMin = returnFunction('minimo')
print(varMin(1,3,5,997,-1))
varAverage = returnFunction('promedio')
print(varAverage(1,3,5,997,-1))