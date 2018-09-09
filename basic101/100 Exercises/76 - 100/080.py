# Exercise 79

import string

rightPass = conditionUpper = conditionNumber = conditionLen = False

while rightPass is not True:
    userPassword = list(input("Enter your password: "))
    if len(userPassword) > 4:
        conditionLen = True
    for char in userPassword:
        if (char in string.ascii_uppercase):
            conditionUpper = True
        if (char in string.digits):
            conditionNumber = True
    if conditionLen and conditionNumber and conditionUpper:
        rightPass = True
    else:
        if conditionUpper is False:
            print("Password is missing an uppercase letter")
        if conditionNumber is False:
            print("Password is missing a number")
        if conditionLen is False:
            print("Password should be at least 5 character long")
    conditionUpper = conditionNumber = conditionLen = False
print("Password sucessfully set!")


