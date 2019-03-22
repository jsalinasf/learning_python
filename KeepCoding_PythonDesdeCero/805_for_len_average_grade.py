def averageListItems(myList):
    sumTotal = 0
    lenMyList = len(myList)
    for i in range(0,lenMyList):
        sumTotal += myList[i]
    return round(sumTotal / lenMyList,2)


myList = (100,90,90,100)
print('Grade list: ',myList)
print('Average Grade',averageListItems(myList))