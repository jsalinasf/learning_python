# Array Practice
rooms = {}

rooms[0, 0] = "Room 1"
rooms[0, 1] = "Room 2"
rooms[0, 2] = "Room 3"
rooms[0, 3] = "Room 4"
rooms[1, 0] = 6.00
rooms[1, 1] = 7.00
rooms[1, 2] = 3.50
rooms[1, 3] = 4.50
rooms[2, 0] = "Monday"
rooms[2, 1] = "Tuesday"
rooms[2, 2] = "Friday"
rooms[2, 3] = "Saturday"


print(rooms)
print("{} entrance cost is: ${} and goes under maintenance on: {}".format(rooms[0, 0], rooms[1, 0], rooms[2, 0]))
print("{} entrance cost is: ${} and goes under maintenance on: {}".format(rooms[0, 1], rooms[1, 1], rooms[2, 1]))
print("{} entrance cost is: ${} and goes under maintenance on: {}".format(rooms[0, 2], rooms[1, 2], rooms[2, 2]))
print("{} entrance cost is: ${} and goes under maintenance on: {}".format(rooms[0, 3], rooms[1, 3], rooms[2, 3]))

i = 0
for i in range(0, 4):
    if rooms[1, i] > 5:
        print(rooms[1, i])

for i in range(0, 3):
    for j in range(0, 4):
        print(rooms[i, j])

