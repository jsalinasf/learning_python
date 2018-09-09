# Exercise 7.8 to 7.10

sandwich_orders = ["pastrami", "tuna", "pastrami", "italian sub", "meat lovers", "vegetarian", "pastrami"]
finished_sandwich = []

print(sandwich_orders)
print(finished_sandwich)

while sandwich_orders:
    sandwich_prepared = sandwich_orders.pop()

    if sandwich_prepared == "pastrami":
        print("Sorry, We run out of {}".format(sandwich_prepared))
        while "pastrami" in sandwich_orders:
            sandwich_orders.remove("pastrami")
            continue
    else:
        finished_sandwich.append(sandwich_prepared)
        print("I made the {} sandwich for you".format(sandwich_prepared).format())

print(sandwich_orders)
print(finished_sandwich)

# Exercise 7.10
poll = {}
answer = True

while answer:
    person_name = input("What's your name: ")
    person_place = input("What's your favorite place for vacation?: ")
    poll[person_name] = person_place
    poll_continue = input("Is anyone else taking the poll (yes / no)?: ")
    if poll_continue == "no":
        answer = False

for name, place in poll.items():
    print("{}'s favorite place to go on a vacation is: {}".format(name, place))
