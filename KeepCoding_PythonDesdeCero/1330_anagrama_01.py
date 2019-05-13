def isAnagramBasic(word1, word2):
    if len(word1) != len (word2):
        return False
    
    myResult = []    

    for letter1 in word1:     
        foundLetter = False
        for letter2 in word2:            
            if letter1 == letter2:
                myResult.append(True)
                foundLetter = True
                break        
        if not foundLetter:
            myResult.append(False)
            foundLetter = False    
    if False in myResult:
        return False
    return True

def isAnagram(word1, word2):
    # This solution is not very efficient but it works
    return isAnagramBasic(word1,word2) and isAnagramBasic(word2, word1)

print(isAnagram('amor','roma')) # True
print(isAnagram('amir','roma')) # False
print(isAnagram('amar','roma')) # False