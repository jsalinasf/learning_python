# Exercises 8.1 to 8.5


def display_message():
    """ Print Message """
    print("I'm learning python functions!")

display_message()


def favorite_book(title):
    """ Print Book """
    print("ONe of my favorite books is {}".format(title))

favorite_book("Python Crush Course")


def make_shirt(shirt_size, shirt_message):
    """ Accept size & message to be printed on Shirt """
    print("Im going to build a shirt size {} with the following message: {}".format(shirt_size, shirt_message))

make_shirt("S", "No Fear")
make_shirt(shirt_size="M", shirt_message="Daredevil rules!")


def make_shirt_defaults(shirt_size="L", shirt_message="I love Python!"):
    """ Accept size & message to be printed on Shirt """
    print("Im going to build a shirt size {} with the following message: {}".format(shirt_size, shirt_message))

make_shirt_defaults()
make_shirt_defaults(shirt_size="M")
make_shirt_defaults(shirt_size="S", shirt_message="Afraid are you?")


def describe_city(city_name, city_country="Ecuador"):
    """ Printing city description """
    print("{} is in {}".format(city_name, city_country))

describe_city("Quito")
describe_city("Guayaquil")
describe_city(city_name="Bogota", city_country="Colombia")
describe_city("Lima", "Peru")