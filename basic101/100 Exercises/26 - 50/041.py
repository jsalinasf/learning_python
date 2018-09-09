# Exercise 41


import string


path = "exercise_41.txt"
file_txt = open(path, "w")

for letter in string.ascii_lowercase:
    file_txt.write(letter + "\n")

file_txt.close()

