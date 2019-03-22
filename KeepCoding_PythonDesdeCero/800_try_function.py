myList = (2,4,6,8)

def ifExists(myList, myIndex):
    try:
        myResult = myList[myIndex]
    except:
        myResult = None
    return myResult

# print(ifExists(myList,0))
# print(ifExists(myList,1))
# print(ifExists(myList,2))
# print(ifExists(myList,3))
# print(ifExists(myList,4)) # It doesn't exist, returns NONE



