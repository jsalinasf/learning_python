# Working with lists of Numbers

# Pay attention to the range() function

# Pay attention to the min(), max() and sum() functions as well

for value in range(1, 5, 1):
    print(value)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

numbers = []
for value in range(1, 251):
    numbers.append(value)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))

# Ver codigo para generar SQUARES - Lines 10
print("\nList Comprehension")
squares2 = [value ** 2 for value in range(1,11)]
print(squares2)