# Exercise 10.2 use replace() method

filename = "youcan.txt"

with open(filename) as file_object:
    list = file_object.readlines()

for line in list:
    print(line.strip())
    print(line.strip().replace("Python", "JavaScript"))
