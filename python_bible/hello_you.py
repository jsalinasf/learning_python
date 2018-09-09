# Ask User for name
user_name = input("whats is your name?: ")

# Ask user for age
user_age = input("How old are you?: ")

# Ask user for city
user_city = input("What City do you live in?: ")

# Ask user what they enjoy
user_love = input ("What do you love doing?: ")

# Create Output Text - OJO al uso de "{} - {}".format(A,B)
string = "Your Name is {} and you are {} years old. You live in {} and you love {}"
#string = "Your Name is {0} and you are {1} years old. You live in {2} and you love {3}"
output = string.format(user_name,user_age,user_city,user_love)

# Print output to screen

print (output)
