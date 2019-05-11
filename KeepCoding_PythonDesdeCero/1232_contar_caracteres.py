myText = 'tres palabras para ti'

myDict = dict()

for letter in myText:
    if letter != ' ':
        if letter in myDict:
            myDict[letter] += 1    
        else:
            myDict[letter] = 1

for key in myDict.keys():
    print(key,'-',myDict[key])
