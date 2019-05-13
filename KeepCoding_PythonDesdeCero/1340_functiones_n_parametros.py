def getAverage(myList):
    mySum = 0
    for n in myList:
        mySum += n
    return mySum / len(myList)

# use the following when you don't know ho wmany parameters the function is going to receive
def getAverageMultipleParameters(*items):
    mySum = 0
    for n in items:
        mySum += n
    return mySum / len(items)



myGrades = (100,100,90,90)

print(getAverage(myGrades))
print(getAverageMultipleParameters(100,100,50,50))