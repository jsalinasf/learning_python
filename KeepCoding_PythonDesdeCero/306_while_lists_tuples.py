
# TUPLES 
# Are defined using () 'parenthesis()'
# Are IMMUTABLE
# Can NOT be Changed on execution time
# Its data Can ONLY be queried, but NOT updated or changed
tupleMonths = ('January','February','March','April','May','June','July','August','September','October','November','December')

# LISTS
# Are defined using [] 'square brackets []'
# Are Mutable
# Can be Changed on execution time
# Its data can be queried, updated or changed at any time
listMonths = [31,28,31,30,31,30,31,31,30,31,30,31]

name = input('What is your name?: ')
print('Hello',name)

userAge = int(input('How old are you?: '))
nowYear = int(input('What is the current year?: '))
nowMonth = int(input('What is the current month?: '))
nowDay = int(input('What is the current day?: '))

daysSoFar = 0
myIndex = 0

while  myIndex < nowMonth - 1:
    daysSoFar += listMonths[myIndex]
    myIndex += 1

daysSoFar += nowDay

userProb = (daysSoFar / 365) * 100
userBorn = nowYear - userAge

print(name, 'you were born in', userBorn,'with a probability of',userProb)
print('or in',userBorn - 1,'with a probability of',100-userProb)