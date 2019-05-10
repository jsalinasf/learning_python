def myUpper(myString):
    newString = ''    
    for letter in myString:
        # ord() -> grabs ascii code from character
        newLetter = ord(letter)
        if newLetter >= 97 and newLetter < 122:
            newLetter = ord(letter) - 32
            # chr() -> converts ascii code into character
            newString += chr(newLetter)
        else:
            newString += letter
    return newString

def myLower(myString):
    newString = ''    
    for letter in myString:
        # ord() -> grabs ascii code from character
        newLetter = ord(letter)
        if newLetter >= 65 and newLetter < 91:
            newLetter = ord(letter) + 32
            # chr() -> converts ascii code into character
            newString += chr(newLetter)
        else:
            newString += letter
    return newString


print(myUpper('abc 1- coco'))
print(myLower('X Y Z and CoCo'))
