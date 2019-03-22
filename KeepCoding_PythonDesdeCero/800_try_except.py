grades = (1,2,3,4)

print(grades[0]) # it works
print(grades[1]) # it works
print(grades[2]) # it works
print(grades[3]) # it works

try:
    print(grades[4]) # error, raises and exception
except:
    print('Out of range')




