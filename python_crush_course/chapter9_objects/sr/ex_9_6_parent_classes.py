# Exercises 9.6 to 9.9

# Classes to use in Exercises

class Restaurant():
    """ An attempt to model a restaurant """

    def __init__(self, name, cousine):
        """ Initialize Object with Name, Cousine and Clients Server """
        self.name = name
        self.cousine = cousine
        self.number_served = 0

    def describe_restaurant(self):
        """ Describing the object info"""
        print("\n{}\nCocina: {}\nClients Served: {}".format(self.name, self.cousine, self.number_served))

    def open_restaurant(self):
        """ Opening the Restaurant """
        print("{} is now Open!".format(self.name))

    def set_number_server(self, new_number_served):
        """ Setting the number of Customers Serverd """
        self.number_served = new_number_served

    def increment_number_served(self, customers_increment):
        """ Increment the Number of customers Served """
        self.number_served += customers_increment

class UserProfile():
        """ Attempt to model a User Profile object """

        def __init__(self, first, last, city, genre):
            self.first = first
            self.last = last
            self.city = city
            self.genre = genre
            self.login_attempts = 0

        def describe_user(self):
            print("\nName: {} {}\nGenre: {}\nCity: {}\nLogin Attempts: {}".format(self.last, self.first, self.genre, self.city, self.login_attempts))

        def greet_user(self):
            print("Welcome {} {}!".format(self.first, self.last))

        def increment_login_attempts(self):
            self.login_attempts += 1

        def reset_login_attempts(self):
            self.login_attempts = 0


# Exercise 9.6 - Ice Cream stand


class IceCreamStand(Restaurant):
    """ Represents aspects of a Restaurant, specific to Ice Cream Stands"""

    def __init__(self, name, cocina):
        super().__init__(name, cocina)
        """
        Initialize attributes of the parent class
        Then initialize attributes of the specific class IceCreamStand
        """
        self.flavors = []

    def add_flavors(self):
        """ Builds List of flavors available at the Ice Cream Stand"""
        print("\nAdd Available Flavors")
        option = ""
        list_flavors = []
        while option != "n":
            option = input("Name ('n' to exit): ")
            if option == "n":
                break
            else:
                list_flavors.append(option)
        self.flavors = list_flavors[::]

    def show_flavors(self):
        i = 0
        print("Available Flavors: ")
        for flavor in self.flavors:
            print(flavor)
        # while i < len(self.flavors):
        #     print(self.flavors[i])
        #     i += 1

stand01 = IceCreamStand("Helado Oscuro", "Ecuatoriana")
stand01.add_flavors()
stand01.set_number_server(100)  # Using Parent Class methods
stand01.increment_number_served(100)  # Using Parent Class methods
stand01.describe_restaurant()  # Using Parent Class methods
stand01.show_flavors()


# Exercise 9.7


class Admin(UserProfile):
    """ Defines a special type of User: Admin"""

    def __init__(self, name, lastname, city, genre):
        super().__init__(name, lastname, city, genre)
        """
        Initialize attributes of the parent class
        Then initialize attributes of the specific class Admin
        """
        self.privileges = []

    def add_privileges(self):
        """ Add Admin Privileges over the system """
        option = ""
        list_privileges = []
        while option != "n":
            option = input("Add Privilege ('n' to quit): ")
            if option == "n":
                break
            else:
                list_privileges.append(option)
        self.privileges = list_privileges[::]

    def show_privileges(self):
        """ Shows Admins Privileges """
        i = 0
        print("Privileges:")
        while i < len(self.privileges):
            print(self.privileges[i])
            i += 1

    def describe_user(self):
        super().describe_user()
        self.show_privileges()

admin01 = Admin("Jorge", "Salinas", "Quito", "Male")
admin02 = Admin("Rodrigo", "Figueroa", "Buenos Aires", "Male")

print("\nSetting Privileges for: {} {}".format(admin01.first, admin01.last))
admin01.add_privileges()
print("\nSetting Privileges for: {} {}".format(admin02.first, admin02.last))
admin02.add_privileges()

admin01.describe_user()
admin02.describe_user()


# Exercise 9.8
