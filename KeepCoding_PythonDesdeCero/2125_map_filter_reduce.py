########################################################################################
# MAP
# Realice una operacion sobre cada uno de los miembros de la lista
# Retorna un conjunto de datos, cuyos items fueron modificados por la FUNCION / OPERACION
########################################################################################

def transformNegative(myNum):
    return myNum * -1

myList = [1, 3, -1, 15, 9]

# map(operacion a realizar, sobre quien realiza la operacion)

# Map con funcion Lambda
myListDoubles = map(lambda x: x*2, myList)
print(list(myListDoubles))

# Map con funcion Normal
myListNegatives = map(transformNegative,myList)
print(list(myListNegatives))



########################################################################################
# FILTER
# Aplica una funcion al conjunto de datos de origen y filtra los items que cumplan con una CONDICION
# Retorna un conjunto de datos SOLAMENTE con aquellos items que pasaron el filtro
#
# IMPORTANTE:  --> La FUNCION (lambda o normal) que aplica el filtro debe retornar TRUE OR FALSE
#
#########################################################################################

def isEven(x):
    return x % 2 == 0

myList2 = [1,4,6,5,8,9,0,1]

# Filtra numeros pares con una funcion lambda
myListEven = filter(lambda x: x % 2 == 0, myList2)
print(list(myListEven)) # Imprime solo 4, 6, 8, 0, los demas items de myListEven fueron excluidos


# Filtra numeros pares con una funcion normal
myListEven2 = filter(isEven, myList2)
print(list(myListEven2)) # Imprime solo 4, 6, 8, 0, los demas items de myListEven fueron excluidos



########################################################################################
# REDUCE
# Aplica una funcion al conjunto de datos de origen y produce un SOLO resultado con dichos items
# 
#########################################################################################

from functools import reduce

mySumList = [10,200,30,5]

myTotalSum = reduce(lambda x,y: x+y, mySumList)
# Fijate aqui como solo devuelve un valor y ya no necesito hacer el cast de "list"
print(myTotalSum)

mySumHundred = reduce(lambda x,y: x+y, range(101))
print(mySumHundred)