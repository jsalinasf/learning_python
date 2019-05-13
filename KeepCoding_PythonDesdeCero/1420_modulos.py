# 1. Import whole module
# import math
# myNum = int(input('Your number: '))
# print(math.factorial(myNum))


# 2. Import specific function from module
# from math import factorial
# myNum = int(input('Your number: '))
# print(factorial(myNum))

# 3. Import specific function from module using ALIAS
from math import factorial as myFact
myNum = int(input('Your number: '))
print(myFact(myNum))

