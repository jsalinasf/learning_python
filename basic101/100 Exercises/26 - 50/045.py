# Exercise 45

import string
import os

if not (os.path.exists("exercise_45")):
    os.makedirs("exercise_45")

for i in string.ascii_lowercase:
    file_name = "exercise_45/" + i + ".txt"
    with open(file_name, "w") as file:
        file.write(i)
    file.close()
