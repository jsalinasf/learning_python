# Exercises 7.1 to 7.3

prompt = "What brand of car would you like to rent?: "
brand_car = input(prompt)
print("Let me see if I can find a {}".format(brand_car).strip().title())

prompt = "How big is your party?: "
party = input(prompt)
party = int(party)
if party < 8:
    print("The table is ready!")
else:
    print("you will have to wait for a table")

prompt = "Enter a number to check if it is a multiple of ten (10): "
number = input(prompt)
number = int(number)
if number % 10 == 0:
    print("{} is a multiple of ten".format(number))
else:
    print("{} is NOT a multiple of ten".format(number))
