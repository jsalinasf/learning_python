
# Data Input
isValid = False
strNumber01 = input('Enter Number 01: ')

while (isValid == False):
    if strNumber01.isdigit():
        number01 = int(strNumber01)
        isValid = True
    elif strNumber01[0] == '-' and strNumber01[1:].isdigit():
        number01 = int(strNumber01)
        isValid = True
    else:
        print('ERROR:',strNumber01,'is not an integer')
        strNumber01 = input('Enter Number 01 again: ')

isValid = False
strNumber02 = input('Enter Number 02: ')

while (isValid == False):
    if strNumber02.isdigit():
        number02 = int(strNumber02)
        isValid = True
    elif strNumber02[0] == '-' and strNumber02[1:].isdigit():
        number02 = int(strNumber02)
        isValid = True
    else:
        print('ERROR:',strNumber02,'is not an integer')
        strNumber02 = input('Enter Number 02 again: ')


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