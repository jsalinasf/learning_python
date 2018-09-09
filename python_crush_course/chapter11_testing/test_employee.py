# Exercise 11.3 - Test Class funtionality

"""

YOU MUST RUN THIS SCRIPT FROM THE TERMINAL

python test_employee.py

"""

import unittest
from employee_functions import Employee

class TestClassEmployee(unittest.TestCase):
    """ Tests for the Employee Class functionality """

    def setUp(self):
        """
        Create an Employee and a set of salaries for use in all methods
         """
        self.employee_01 = Employee("John", "Smith", 2500)
        self.employee_02 = Employee("Carl", "Marine", 3500)

    def test_give_raise_default(self):
        default_raise = 5000
        old_salary = self.employee_01.employee_salary
        new_salary = self.employee_01.give_raise()
        self.assertEqual(old_salary + default_raise, new_salary)

    def test_give_raise_custom(self):
        custom_raise = 1500
        old_salary = self.employee_02.employee_salary
        new_salary = self.employee_02.give_raise(custom_raise)
        self.assertEqual(old_salary + custom_raise, new_salary)

unittest.main()