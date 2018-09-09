# Exercise 9.9

class Car():
    """ An attempt to define a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        print("This car has {} kms on it".format(self.odometer))

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer += miles

class Battery():
    """ An attempt to define a Battery Object """

    def __init__(self, battery_size=70):
        """ Initialize Battery Attributes """
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
        else:
            print("Battery can't be upgraded")

    def describe_battery(self):
        """ Prints a statement containing battery info"""
        print("This car has a {} -kWh battery".format(self.battery_size))

    def get_range(self):
        """ Prints a statement containing the range this battery provides """

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This can can go approximately {} miles ".format(range)
        message += "on a full charge"
        print(message)

class ElectricCar(Car):
    """ Represents aspects of a car, specific to an Electric Car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an Electric Car
        """
        self.battery = Battery()

my_tesla = ElectricCar("Tesla", "Model S", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
print("\nUpgrading Battery, hold on...done\n")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()