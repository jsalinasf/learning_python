# Exercise 46

import glob

the_list = []

file_list = glob.glob("exercise_45/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        the_list.append(file.read().strip("\n"))
    file.close()

print(the_list)