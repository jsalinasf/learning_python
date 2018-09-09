# Exercise 5.1 to
car = "subaru"
print("\nIs car == 'subaru'? I predict True")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False")
print(car == "audi")

print("\n")
print("casa" == "casa")
print("casa" != "casa")

print("\nExiste un elemento en la lista?")
ingredients = ["Cheese", "Pepperoni", "Sausage", "Onions"]
print(ingredients)
print("\nLooking for Cheese")
print("Cheese" in ingredients)
print("\nLooking for Meat")
print("Meat" in ingredients)
print("\nConfirming that Meat is NOT in the list")
print("Meat" not in ingredients)
if ("Cheese" in ingredients) and ("Pepperoni" in ingredients):
    print("This pizza has Cheese & Pepperoni")
if ("Cheese" in ingredients) and ("Meat" not in ingredients):
    print("This pizza has Cheese but not Meat")
if ("Cheese" in ingredients) or ("Meat" in ingredients):
    print("This pizza may have Cheese OR Meat")
