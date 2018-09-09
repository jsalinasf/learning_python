# Exercise 9.10 Importing Restaurant Class

from restaurant import Restaurant

r1 = Restaurant("El Moco Loco", "Ecuatoriana")

r1.describe_restaurant()
r1.open_restaurant()
r1.set_number_server(100)
r1.increment_number_served(50)
r1.describe_restaurant()

r2 = Restaurant("Cascaritas Cuencanas", "Ecuatoriana")
r2.describe_restaurant()
r2.open_restaurant()
r2.set_number_server(15)
r2.describe_restaurant()
r2.increment_number_served(15)
r2.describe_restaurant()

