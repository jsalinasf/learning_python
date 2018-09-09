# Exercise 10.11 - json - favorite number
import json

print("I'll try to guess your favorite number...")
file_name = "favorite_number.txt"

try:
    with open(file_name) as file_object:
        favorite_number = json.load(file_object)

except FileNotFoundError:
    print("This is embarrassing, I can't guess your favorite number :(")

else:
    print("Your favorite number is: {}".format(favorite_number))
