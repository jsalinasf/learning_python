# Exercise 10.3 - Writing Files - Guest
import datetime

filename = "guests.txt"
user_name = ""

while user_name != "n":
    user_name = input("What is your Name ('n' to quit): ")
    if user_name != "n":
        with open(filename, "a") as file_object:  # In here Im using "APPEND"
            log = user_name + "\tarrived on\t" + str(datetime.datetime.now())
            file_object.write(log + "\n")
        print("Welcome {}".format(user_name))
