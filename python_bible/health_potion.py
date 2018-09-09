import random

health = 50

#1 easy, 2 medium, 3 hard
difficulty = 3

potion_health = int((random.randint(25, 50)) / difficulty)

health = health + potion_health

#print(potion_health)
print(health)


