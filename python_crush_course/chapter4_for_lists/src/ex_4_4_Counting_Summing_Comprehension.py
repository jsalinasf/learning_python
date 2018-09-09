# Exercises 4.3 to 4.9

for value in range(1, 21):
    print(value)

print("\nCounting up to a Million")
million = []
for value in range(1, 1000001):
    million.append(value)
print(min(million))
print(max(million))
print(sum(million))
print(len(million))

print("\nOdd Numbers")
for value in range(0, 21, 2):
    print(value)

print("\nThrees")
for value in range(0, 33, 3):
    print(value)

print("\nCubes and List Comprehension")
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# List SLICES
print(cubes[-3:])
print(cubes[2:5])
for number in cubes[3:8]:
    print(number)