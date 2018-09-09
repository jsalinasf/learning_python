# Exercise 10.9 - SILENTLY try-except blocks - Cats & Dogs

filename_01 = "dogs.txt"
filename_02 = "cats2.txt"

try:
    with open(filename_01) as file_object01:
        name_dogs = file_object01.read()
except FileNotFoundError:
    pass

else:
    print(name_dogs)

try:
    with open(filename_02) as file_object02:
        name_cats = file_object02.read()

except FileNotFoundError:
    pass

else:
    print(name_cats)

