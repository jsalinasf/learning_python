# Exercise 11.1 - test function - file: city_functions.py

"""

YOU MUST RUN THIS SCRIPT FROM THE TERMINAL

python test_cities.py

"""

import unittest
from city_functions import get_city_country


class CityCountryTest(unittest.TestCase):

    """ Test for city_functions.py """

    def test_city_country(self):
        """ Do City and Country like guayaquil and ecuador work? """
        formatted_name = get_city_country("guayaquil", "ecuador")
        self.assertEqual(formatted_name, "Guayaquil, Ecuador")

    def test_city_country_population(self):
        """ Do City, Country and Population like Guayaquil, Ecuador, 150000 work?"""
        formatted_name = get_city_country("Guayaquil", "Ecuador", 150000)
        self.assertEqual(formatted_name, "Guayaquil, Ecuador, Population: 150000")

unittest.main()

