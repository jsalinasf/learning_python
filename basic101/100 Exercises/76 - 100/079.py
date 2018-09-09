# Exercise 79

import string

rightPass = condition_1 = condition_2 = False

print("\nPassword should meet the following criteria:")
print("* Be at least 5 character long")
print("* Contain at least one uppercase letter")
print("* Contain at least one number\n")

# while rightPass is not True:
#   userPassword = list(input("Enter your password: "))
#   if len(userPassword) < 5:
#     continue
#   else:
#     for char in userPassword:
#       if (char in string.ascii_uppercase):
#         condition_1 = True
#       if (char in string.digits):
#         condition_2 = True
#   if condition_1 and condition_2:
#     rightPass = True
#   else:
#     print("Password not Fine, Try again please")

# print("Your new password has been set!")

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
