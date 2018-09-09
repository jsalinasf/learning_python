# Exercise 10.11 - json - favorite number
import json

favorite_number = int(input("What is your favorite number?: "))
file_name = "favorite_number.txt"

try:
    with open(file_name, "w") as file_object:
        json.dump(favorite_number, file_object)

except FileNotFoundError:
    print("There is an error trying to save your number")

else:
    print("Your favorite number has been saved")
