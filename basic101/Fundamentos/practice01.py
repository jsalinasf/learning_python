print("Hello World")
shirt1 = 14.99
print(shirt1)
shirt1 += 1
print(shirt1)
shirt1 *= 1.25
print(shirt1)

age = 35
message = "Your age is: "
print("Your age is: " + str(age))

slogan = "Just do it!"
print(slogan)

price = 60
tax = 12
discount = 10

# without Variables
print("\nPrice: $ {}".format(price))
print("{}% Discount: $ {}".format(discount, price * (discount / 100)))
print("Subtotal: $ {}".format(price - (price * (discount / 100))))
print("{} % Tax: $ {}".format(tax, (price - (price * (discount / 100))) * (tax / 100)))
print("Total: $ {}".format(((price - (price * (discount / 100))) + (price - (price * (discount / 100))) * (tax / 100))))

# Using accumulative operators
print("\nPrice: $ {}".format(price))
aux = discount
discount = price * (discount/100)
print("{}% Discount: $ {}".format(aux, discount))
price -= discount
print("Subtotal: $ {}".format(price))
aux = tax
tax = price * (tax/100)
print("{}% Tax: $ {}".format(aux, tax))
price += tax
print("Total: $ {}".format(price))

