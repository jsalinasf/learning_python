myList = (2,4,6,8)

def listContains(myList, myIndex):
    try:
        myResult = myList[myIndex]
    except:
        myResult = None
    return myResult

# Count myList items
i = 0
while listContains(myList, i) != None:
    print(myList[i])
    i += 1
    
print('Items count:',i)


