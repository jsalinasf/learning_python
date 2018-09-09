# Bucles

attempts = 0
user01 = ""
password = "coco"

while attempts < 3:
    user01 = input("Input your password: ")
    if user01 == password:
        print("Granted access!")
        break
    else:
        print("Wrong Password. You have {} attempts left".format(2 - attempts))
    attempts += 1

price = input("House Price $: ")
price = float(price)
category = input("House Category: ")

if category == "A":
    price *= 1.1
elif category == "B":
    price *= 1.2
elif category == "C":
    pass
elif category == "D":
    price *= 0.9
elif category == "E":
    price *= 0.8
else:
    pass
print("Final price $: {}".format(price))
