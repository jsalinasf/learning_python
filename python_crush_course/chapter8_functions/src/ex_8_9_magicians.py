# Exercises 8.9 to 8.11


# Exercise 8.9 and 8.10
def display_magicians(wizards):
    """ Prints Magician from the given list """
    aux = len(wizards)
    for i in range(0, aux):
        wizards[i] = "The Great " + wizards[i]

wizards = ["White", "Black", "Sauron", "Mickey"]
print(wizards)
display_magicians(wizards)
print("\nOriginal list modified by function")
print(wizards)


# Exercise 8.11
def show_magicians(wizards):
    """ Prints Magician from the given list """
    for magician in wizards:
        magician = "The Great " + magician
        great_wizards.append(magician)

great_wizards = []
wizards = ["White", "Black", "Sauron", "Mickey"]
show_magicians(wizards)
print("\nOriginal list remains the same, it WAS NOT modified by the function")
print(wizards)
print(great_wizards)
