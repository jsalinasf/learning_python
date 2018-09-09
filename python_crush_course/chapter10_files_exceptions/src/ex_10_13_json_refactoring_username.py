# Exercise 10.13 - refactoring - json - username

import json


def get_stored_username():
    """ Get stored Username from json file """

    file_name = "username.json"

    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)

    except FileNotFoundError:
        return None

    else:
        return user_name


def get_new_username():
    """ Prompts and create a new Username"""

    file_name = "username.json"
    user_name = input("What is your username?: ")

    with open(file_name, "w") as file_object:
        json.dump(user_name, file_object)
    print("We'll remember you {} next time!".format(user_name))
    return user_name


def greet_user():
    """ Greet existing User by Name"""
    user_name = get_stored_username()
    if user_name:
        validate_user = input("Are you {} (y/n)?".format(user_name))
        validate_user = validate_user.strip().lower()

        if validate_user == "y":
            print("Welcome back {}!".format(user_name))
        else:
            get_new_username()

    else:
        get_new_username()

greet_user()