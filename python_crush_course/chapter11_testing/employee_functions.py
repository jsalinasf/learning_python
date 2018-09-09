# Exercise 11.3 - Test Class funtionality

class Employee():
    """ An attempt to define an Employee """

    def __init__(self, employee_name, employee_last, employee_salary):
        """ Initialize Employee Object, all param are mandatory """

        self.employee_name = employee_name
        self.employee_last = employee_last
        self.employee_salary = employee_salary

    def give_raise(self, ammount=5000):
        """ Raises Employee's salary. Default raise is 5000 """
        self.employee_salary += ammount
        return self.employee_salary

