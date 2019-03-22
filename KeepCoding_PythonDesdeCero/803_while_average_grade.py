
def listContains(myList, myIndex):
    try:
        myResult = myList[myIndex]
    except:
        myResult = None
    return myResult

def sumListItems(myList):
    i = 0
    sumTotal = 0
    while listContains(myList, i) != None:
        sumTotal += myList[i]
        i += 1
    return sumTotal / i

myList = (2,4,6,8,10,12)
print('Grade list: ',myList)
print('Average Grade',sumListItems(myList))


