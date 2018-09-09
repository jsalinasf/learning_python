# Exercise 5.3 to 5.7
import random

alien_color = "red"  # green, yellow or red
if alien_color == "green":
    print("Player earned 5 points!")
elif alien_color == "yellow":
    print("Player earned 10 points!")
elif alien_color == "red":
    print("Player earned 15 points!")

person_age = random.randrange(0, 80)
print(person_age)
if person_age < 3:
    print("The person is Baby")
elif person_age < 5:
    print("The person is a Toddler")
elif person_age < 13:
    print("The person is a Kid")
elif person_age < 20:
    print("The person is a Tennager")
elif person_age < 66:
    print("The person is an Adult")
elif person_age  > 65:
    print("The person is an Elder")

fruits = ["Apple", "Banana", "Tangerine", "Orange", "Blueberry"]
if "Apple" in fruits:
    print("Adding Apple")
if "Orange" in fruits:
    print("Adding Orange")
if "Blackberry" in fruits:
    print("Adding Blackberry")


