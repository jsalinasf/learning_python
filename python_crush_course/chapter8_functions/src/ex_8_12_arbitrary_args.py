# Exercises 8.12 to 8.14


# Exercise 8.12
def prepare_sandwich(*ingredients):
    """ Print the ingredients of an ordered sandwich """
    print("\nI'll prepare a sandwich withe the following ingredients: ")
    for ingredient in ingredients:
        print("- " + ingredient)

prepare_sandwich("cheese", "tomato", "lettuce", "honey mustard")
prepare_sandwich("pepperoni")
prepare_sandwich("italian beef", "sausage", "ketchup")


#exercise 8.13
def build_profile(first, last, **user_info):
    user_profile = {}
    user_profile["name"] = first
    user_profile["last"] = last
    for key, value in user_info.items():
        user_profile[key] = value
    return user_profile

usuario = build_profile("Jorge",
                        "Salinas",
                        city="Quito",
                        age="36"
              )
print(usuario)

usuario = build_profile("Ale",
                        "Sanchez",
                        workplace="Avis",
                        cellphone="0998766642",
                        mother="Carmita"
              )
print(usuario)

usuario = build_profile("Karen",
                        "Mayorga",
                        University="UDLA"
              )
print(usuario)


# Exercise 8.14
def make_car(car_model, car_manufacturer, **car_details):
    """ Receives mandatory args and a dictionary"""
    car_info = {}
    car_info["model"] = car_model
    car_info["manufacturer"] = car_manufacturer
    for key, value in car_details.items():
        car_info[key] = value
    return car_info

my_car = make_car("Corvette",
                  "Chevrolet",
                  hp="500",
                  racing="yes"
                  )
print(my_car)

my_car = make_car("F150",
                  "FORD",
                  hp="286",
                  type="Pickup Truck",
                  lenght="18 feet",
                  seats="6"
                  )
print(my_car)