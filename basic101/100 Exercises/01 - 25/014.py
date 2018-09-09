# Exercise 14

print("\nSolution 01 - It does not keep an order")
a = ["1", 1, "1", 2]

a = list(set(a))
print(a)

print("\nSolution 02 - It uses OrderDict")
from collections import OrderedDict

a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

print("\nSolution 03")
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
