# Exercise 81

import os
import string

rightUser = False

file_item_path = os.path.join(os.path.dirname(__file__), "users.txt")

fo = open(file_item_path, "r")
Users = fo.read()
fo.close()

while rightUser is not True:
    userName = input("Input a Username: ")
    if userName in Users:
        print("Username has been taken!")
        continue
    else:
        rightUser = True
        break

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

