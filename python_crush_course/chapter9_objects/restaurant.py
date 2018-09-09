""" An attempt to model a restaurant """


class Restaurant():

    def __init__(self, name, cousine):
        """ Initialize Object with Name, Cousine and Clients Server """
        self.name = name
        self.cousine = cousine
        self.number_served = 0

    def describe_restaurant(self):
        """ Describing the object info"""
        print("\n{}\nType: {}\nServed Clients: {}".format(self.name, self.cousine, self.number_served))

    def open_restaurant(self):
        """ Opening the Restaurant """
        print("{} is now Open!".format(self.name))

    def set_number_server(self, new_number_served):
        """ Setting the number of Customers Serverd """
        self.number_served = new_number_served

    def increment_number_served(self, customers_increment):
        """ Increment the Number of customers Served """
        self.number_served += customers_increment
