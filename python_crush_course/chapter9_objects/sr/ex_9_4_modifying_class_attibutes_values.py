# Exercises 9.4 to 9.5

# Exercise 9.4 Adding functionality to Exercise 9.1

class Restaurant():
    """ An attempt to model a restaurant """

    def __init__(self, name, cousine):
        """ Initialize Object with Name, Cousine and Clients Server """
        self.name = name
        self.cousine = cousine
        self.number_served = 0

    def describe_restaurant(self):
        """ Describing the object info"""
        print("\nName: {}\tCousine Type: {}\tClients Served: {}".format(self.name, self.cousine, self.number_served))

    def open_restaurant(self):
        """ Opening the Restaurant """
        print("{} is now Open!".format(self.name))

    def set_number_server(self, new_number_served):
        """ Setting the number of Customers Serverd """
        self.number_served = new_number_served

    def increment_number_served(self, customers_increment):
        """ Increment the Number of customers Served """
        self.number_served += customers_increment

r1 = Restaurant("Pollos Gus", "French")
r1.describe_restaurant()
r1.number_served = 25  # Modifying Attribute directly
r1.describe_restaurant()
r1.set_number_server(100)  # Modifying Attribute through a Method
r1.describe_restaurant()
r1.increment_number_served(1200)
r1.describe_restaurant()


# Exercise 9.4

class UserProfile():
    """ Attempt to model a User Profile object """

    def __init__(self, first, last, city, genre):
        self.first = first
        self.last = last
        self.city = city
        self.genre = genre
        self.login_attempts = 0

    def describe_user(self):
        print("{}\t{}\t{}\t{}\t{}".format(self.last, self.first, self.genre, self.city, self.login_attempts))

    def greet_user(self):
        print("Welcome {} {}!".format(self.first, self.last))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user01 = UserProfile("Papa", "Frita", "Quito", "Male")
user02 = UserProfile("Sarita", "Balboa", "Quito", "Female")
user03 = UserProfile("Shony", "Lopez", "Ambato", "Female")

user01.describe_user()
user02.describe_user()
user03.describe_user()

user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
user02.increment_login_attempts()
user02.increment_login_attempts()
user03.increment_login_attempts()

user01.describe_user()
user02.describe_user()
user03.describe_user()

user01.reset_login_attempts()
user02.reset_login_attempts()
user03.reset_login_attempts()

user01.describe_user()
user02.describe_user()
user03.describe_user()
