# Exercise 3.3 - Lists
# Appending, inserting, deleting and poping Item lists

cars = ["Porshe", "Ferrari", "Audi", "BMW"]

print("I would like to own a " + cars[0] + " car")
print("How much would a " + cars[1] + " cost?")
print("I may afford an old " + cars[2] + "... I guess!")
print("Imagine racing a " + cars[3] + " race car, Legen....dary!")

# Updating an Element List
print("\n")
print(cars)
print("Vamos a cambiar Porshe por Tesla")
cars[0] = "Tesla"
print(cars)

# Appending a New Element list
# Appending adds the element to the end of the list
print("\nLets 'APPEND' Aston Martin to the 'END' of the list!")
cars.append("Aston Martin")
print(cars)

print("\nLets INSERT 'Mini' into the 4th position of the list!")
cars.insert(3, "Mini")
print(cars)

print("\nEliminemos Ferrari")
del cars[1]
print(cars)

print("\n Vamos a hacer POP del 3er elemento de la Lista")
print(cars)
popped_car=cars.pop(2)
print(cars)
print(popped_car + " fue removido de la lista pero lo tengo guardado en una variable para gestionarlo")

print("\nVamos a 'REMOVE' un objeto de la lista por su 'VALOR' - remove(variable) Ejemplo Tesla")
remover_auto = "Tesla"
print(cars)
cars.remove(remover_auto)
print(cars)
print("El auto removido fue: " + remover_auto)
