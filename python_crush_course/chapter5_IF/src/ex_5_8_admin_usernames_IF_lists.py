# Exercises 5.8 to 5.11

users = ["coco", "ale", "karen", "sarita", "admin"]
if users:
    for user in users:
        if user == "admin":
            print("Hello " + user + ", would you like to see a tatus report?")
        else:
            print("Hello " + user + ", thank you for logging")
else:
    print("\nWe need to find some users!")

users = []
if users:
    for user in users:
        if user == "admin":
            print("Hello " + user + ", would you like to see a tatus report?")
        else:
            print("Hello " + user + ", thank you for logging")
else:
    print("\nWe need to find some users!")

current_users = ["luis", "pepe", "gabo", "dani"]
new_users = ["Jota", "LuIS", "Santi", "DANi"]
print(current_users)
print(new_users)
for new_user in new_users:
    print(new_user)
    if new_user.lower() in current_users:
        print("existing user, choose a new one!")
    else:
        print("Your username has been created, welcome!")

numbers = [value for value in range(1, 11)]
print(numbers)
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")