# Exercise 10.8 - try-except blocks - Cats & Dogs

filename_01 = "dogs.txt"
filename_02 = "cats2.txt"

try:
    with open(filename_01) as file_object01:
        name_dogs = file_object01.read()
except FileNotFoundError:
    print("The file '{}' can't be found".format(filename_01))

else:
    print(name_dogs)

try:
    with open(filename_02) as file_object02:
        name_cats = file_object02.read()

except FileNotFoundError:
    print("The file '{}' can't be found".format(filename_02))

else:
    print(name_cats)

