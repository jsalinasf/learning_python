def sumaTodos(limitTo):
    sumaTotal = 0
    for i in range (1,limitTo+1):
        sumaTotal += i
    return sumaTotal

print(sumaTodos(5))
