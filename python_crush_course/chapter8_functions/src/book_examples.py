# Following Book Examples


# Positional Arguments
def describe_pet(animal_type, pet_name):
    """ Display information about a pet """
    print("I have a {} and its name is {}".format(animal_type, pet_name))

describe_pet("Hamster", "Harry el Pelao")
describe_pet(animal_type="dog", pet_name="Lucas")
describe_pet(pet_name="Goliath", animal_type="lady bug")


# Default Values ALWAYS go at the END!!
def describe_pet(pet_name, animal_type="dog"):
    """ Display information about a pet """
    print("I have a {} and its name is {}".format(animal_type, pet_name))

describe_pet("Copito the Killer Machine")




