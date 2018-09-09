# Exercise 11.1 - testing - functions - city - country


def get_city_country(city_name, country_name, city_population=0):
    if city_population > 0:
        formatted_name = city_name + ", " + country_name + ", Population: " + str(city_population)
    else:
        formatted_name = city_name + ", " + country_name
    return formatted_name.title()
