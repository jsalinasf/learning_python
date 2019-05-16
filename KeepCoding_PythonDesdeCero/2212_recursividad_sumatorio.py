def recursiveSum(myNumber):
    if myNumber > 0:
        return myNumber + recursiveSum(myNumber - 1)
    else:
        return 0


def recursiveFactorial(myNumber):
    if myNumber > 1:
        return myNumber * recursiveFactorial(myNumber - 1)
    else:
        return 1

print(recursiveSum(4))
print(recursiveFactorial(4))