# Exercise 9.1 to 9.3

# Exercise 9.1 Restaurant


class Restaurant():
    """ An attempt to model a restaurant """

    def __init__(self, name, cousine):
        """ Initialize name and cousine attributes """
        self.name = name
        self.cousine = cousine

    def describe_restaurant(self):
        """ Describing the restaurant info """
        print("\n{} - Cousine Type: {}".format(self.name, self.cousine))

    def open_restaurant(self):
        """ Simulates opening the restaurant """
        print("{} is now open!".format(self.name))

my_restaurant01 = Restaurant("YaguarCrazys", "Italian")
my_restaurant02 = Restaurant("La Tripa Asesina", "Ecuadorian")
my_restaurant03 = Restaurant("La Delicia Sonada", "Mexican")

# Exercise 9.2 Three Restaurants
my_restaurant01.describe_restaurant()
my_restaurant01.open_restaurant()
my_restaurant02.describe_restaurant()
my_restaurant02.open_restaurant()
my_restaurant03.describe_restaurant()
my_restaurant03.open_restaurant()


# Exercise 9.3 User Profile
class UserProfile():
    """ Attempt to model a User Profile object """

    def __init__(self, first, last, city, genre):
        self.first = first
        self.last = last
        self.city = city
        self.genre = genre

    def describe_user(self):
        print("\n{}, {} - {} - {}".format(self.last, self.first, self.genre, self.city))

    def greet_user(self):
        print("Welcome {} {}!".format(self.first, self.last))

user01 = UserProfile("Papa", "Frita", "Quito", "Male")
user02 = UserProfile("Sarita", "Balboa", "Quito", "Female")
user03 = UserProfile("Shony", "Lopez", "Ambato", "Female")

user01.describe_user()
user01.greet_user()
user02.describe_user()
user02.greet_user()
user03.describe_user()
user03.greet_user()
