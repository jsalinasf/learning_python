# Exercise 77
from datetime import datetime

# date_entry = datetime.strptime(input("Birth date (m/d/y): "), "%m/%d/%Y")
# print("You were born in: " + str(date_entry.year))

age = int(input("Whats is your age: "))

yearOfBirth = datetime.now().year - age

print("You were born in: {}".format(str(yearOfBirth)))
