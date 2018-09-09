# Exercise 10

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# solution 01
# new_letters = []
#
# for i in range(0, len(letters)):
#     if i % 2 == 0:
#         new_letters.append(letters[i])
#
# print(new_letters)

# solution 02
# print(letters[0:len(letters):2]) # My solution
print(letters[::2])  # Instructor solution
