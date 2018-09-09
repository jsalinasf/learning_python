# Exercise 47

import glob

the_list = []
check = "python"

file_list = glob.glob("exercise_45/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        letter = file.read().strip("\n")
        if letter in check:
            the_list.append(letter)
    file.close()
print(the_list)


