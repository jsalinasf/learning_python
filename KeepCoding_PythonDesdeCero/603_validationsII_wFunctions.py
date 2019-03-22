def validInput(myMessage):
    strNumber = input(myMessage)
    isValid = False
    while (isValid == False):
        if strNumber.isdigit():
            myNumber = int(strNumber)
            isValid = True
        elif strNumber != '' and strNumber[0] == '-' and strNumber[1:].isdigit():
            myNumber = int(strNumber)
            isValid = True
        else:
            print('ERROR:',strNumber,'must be an integer')
            strNumber = input(myMessage)
    return myNumber

# Data Input
number01 = validInput('Input Number 01: ')
number02 = validInput('Input Number 02: ')

# Data Processing
mySum = round(number01 + number02, 2)
mySub = round(number01 - number02, 2)
myMul = round(number01 * number02, 2)
myDiv = round(number01 / number02, 2)

# Data Output
print(number01,'+',number02,'=',mySum)
print(number01,'-',number02,'=',mySub)
print(number01,'*',number02,'=',myMul)
print(number01,'/',number02,'=',myDiv)