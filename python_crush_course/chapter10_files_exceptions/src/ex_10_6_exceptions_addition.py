# Exercise 10.6 & 10.7 - Exceptions try-except - Addition

number_01 = ""

while number_01 != "n":
    number_01 = input("Number 1 ('n' to quit): ")

    if number_01 != "n":

        number_02 = input("Number 2: ")

        try:
            add_numbers = int(number_01) + int(number_02)

        except ValueError:
            print("Make sure you input 'numbers'!")

        else:
            print(str(add_numbers))

    else:
        break
