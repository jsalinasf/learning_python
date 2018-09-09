# Exercises 6.7 to 6.12

# Ejercicio 6.7

person_iknow_01 = {
    "first_name": "Manuela",
    "last_name": "Cevallos",
    "age": 8,
    "city": "Quito"
    }

person_iknow_02 = {
    "first_name": "Alejandra",
    "last_name": "sanchez",
    "age": 38,
    "city": "Quito"
    }

person_iknow_03 = {
    "first_name": "Carmen",
    "last_name": "Ocana",
    "age": 58,
    "city": "ambato"
    }

group_persons = [person_iknow_01, person_iknow_02, person_iknow_03]

for person in group_persons:
    print(person)

# Ejercicio 6.8

sarita = {
    "owner": "ale",
    "type": "dog",
    "age": 2,
    "city": "quito"
}

bony = {
    "owner": "gabi",
    "type": "dog",
    "age": 10,
    "city": "ambato"
}

copito = {
    "owner": "carmita",
    "type": "dog",
    "age": 1,
    "city": "ambato"
}

pets = [sarita, bony, copito]

for pet in pets:
    print(pet["owner"], pet["type"], pet["age"], pet["city"])

# Ejercicio 6.9

favorite_places = {
    "coco": ["paris", "roma", "berlin"],
    "ale": ["new york", "galapagos"],
    "karen": ["el mercado de ambato"]
}

for person, lugares in favorite_places.items():
    print("\nLos lugares favoritos de {} son:".format(person).title())
    for lugar in lugares:
        print(lugar.title())

# Ejercicio 6.10

favorite_numbers = {
    "ale": [18, 25, 31],
    "coco": [7, 21],
    "karen": [3],
    "manuela": [1, 5, 9, 99]
}

for nombre, numeros in favorite_numbers.items():
    print("Los numeros favoritos de {} son:".format(nombre).title())
    print(numeros)

# Ejercicio 6.11

cities = {
    "quito": {"poblacion": 1500, "pais": "ecuador", "fact": "ubicada a 2600 msnm"},
    "new york": {"poblacion": 17720, "pais": "usa", "fact": "ubicada a 10 msnm"},
    "pekin": {"poblacion": 23500, "pais": "china", "fact": "ubicada a 1200 msnm"}
}

for city, facts in cities.items():
    print("\n{}".format(city).title())
    poblacion = facts["poblacion"]
    pais = facts["pais"]
    msnm = facts["fact"]
    print("Tiene {} habitantes, Pais: {} y esta a {} metros sobre nivel del mar"
          .format(poblacion, pais, msnm).title())

