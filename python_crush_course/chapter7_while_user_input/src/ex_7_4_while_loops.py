# Exercises 7.4 to 7.7

flag = True
topping_pizza = ""
while flag:
    if topping_pizza == "quit" or topping_pizza == "Quit" or topping_pizza == "QUIT":
        flag = False
    else:
        topping_pizza = input("Enter a Pizza Topping: ")
        print("I'll add {} to the pizza".format(topping_pizza).title().strip())

edad_persona = 0
while True:
    edad_persona = input("How old are you?: ")
    if edad_persona == "quit":
        break
    else:
        edad_persona = int(edad_persona)
        if edad_persona < 3:
            print("You ticket is free")
        elif edad_persona < 13:
            print("Your ticket cost is $10")
        elif edad_persona > 12:
            print("Your ticket cost is $15")
