# Exercise 78
import random
import string

seed = string.ascii_lowercase + string.digits + string.ascii_uppercase + "!@#$%*()?"

chosen = random.sample(seed, 6)

password = "".join(chosen)

print(password)

