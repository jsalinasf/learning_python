
# Input Data
strNumber01 = input('Enter one number: ')
strNumber02 = input('Enter another number: ')

# Processing Data
if strNumber01.isdigit():
    number01 = int(strNumber01)
elif strNumber01[0] == '-' and strNumber01[1:].isdigit():
    number01 = int(strNumber01)
else:
    print(strNumber01,'is not an integer')
    quit()

if strNumber02.isdigit():
    number02 = int(strNumber02)
elif strNumber02[0] == '-' and strNumber02[1:].isdigit():
    number02 = int(strNumber02)
else:
    print(strNumber02,'is not an integer')
    quit()

mySum = round(number01 + number02, 2)
mySub = round(number01 - number02, 2)
myMul = round(number01 * number02, 2)
myDiv = round(number01 / number02, 2)

# Output Data
print(number01,'+',number02,'=',mySum)
print(number01,'-',number02,'=',mySub)
print(number01,'*',number02,'=',myMul)
print(number01,'/',number02,'=',myDiv)