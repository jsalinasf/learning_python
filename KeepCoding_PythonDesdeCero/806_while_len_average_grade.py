def averageListItems(myList):
    sumTotal = 0
    i = 0
    lenMyList = len(myList)
    while i < lenMyList:
        sumTotal += myList[i]
        i += 1
    return round(sumTotal / lenMyList,2)


myList = (100,80,80,100)
print('Grade list: ',myList)
print('Average Grade',averageListItems(myList))