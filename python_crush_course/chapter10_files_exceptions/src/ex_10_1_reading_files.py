# Exercise 10.1 - Learning Python, Reading From Files

filename = "youcan.txt"

# Reading an ENTIRE file
print("\nReading an ENTIRE file")
with open(filename) as file_object:
    contents = file_object.read()
print(contents.rstrip())


# Reading Line by Line
print("\n#Reading Line by Line")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Making a list from file
print("\nMaking a List")
with open(filename) as file_object:
    list = file_object.readlines()

for line in list:
    print(line.rstrip())