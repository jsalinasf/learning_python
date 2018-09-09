# Exercise 10.12 - json - favorite number remembered

import json

file_name = "favorite_number.json"

try:
    with open(file_name) as file_object:
        favorite_number = json.load(file_object)

except FileNotFoundError:
    favorite_number = input("What is your favorite number?: ")
    with open(file_name, "w") as file_object:
        json.dump(favorite_number, file_object)
    print("We'll remember your favorite number")

else:
    print("Your favorite number is: {}".format(favorite_number))