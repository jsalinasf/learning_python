# Exercise 10.10 - try-except blocks - Common words

filename = "alice.txt"

try:
    with open(filename) as file_object:
        content = file_object.read()

except FileNotFoundError:
    print("The file '{}' doesn't exist".format(filename))

else:
    print("The Word 'Alice' appears {} times in '{}'".format((content.lower().count("alice")), filename))


