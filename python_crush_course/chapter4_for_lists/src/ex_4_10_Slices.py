# Exercises 4.10 to 4.12

cars = ["BMW", "Mercedes Benz", "Chevrolet", "Ford", "Jeep", "Ferrari", "Nissan", "Tesla", "Peugeot"]
print(cars)
print("\nThe first three items in the list are:")
print(cars[:3])
print("\nThe middle three items in the list are:")
print(cars[3:6])
print("\nThe last three items in the list are:")
print(cars[-3:])

friend_cars = cars[::]
cars.append("Toyota")
friend_cars.append("Hyundai")
print("\nMy favorite cars are:")
for car in cars:
    print(car)
print("\nMy Friend's favorite cars are:")
for car in friend_cars:
    print(car)

# Working with TUPLES
print("\nWorking with TUPLES")
menus = ("Tallarin", "arroz", "carne frita", "bolon", "pollo")
for menu in menus:
    print(menu)

# Error -> Las TUPLAS son inmutables, no se pueden cambiar sus elementos
# menus[3] = "Papitas Fritas"

print("\nLa unica manera de cambiar una TUPLA es reasignando TODO la TUPLA")
menus = ("Canguil", "Cola", "Hot Dogs", "Caucaras")
for menu in menus:
    print(menu)



