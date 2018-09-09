# Exercises 6.1 to 6.3

person_know = {
    "first_name": "Manuela",
    "last_name": "Cevallos",
    "age": 8,
    "city": "Quito"
    }

favorite_numbers = {
    "ale": 18,
    "coco": 7,
    "karen": 31,
    "manuela": 8
}

print("Ale: " + str(favorite_numbers["ale"]))
print("Coco: " + str(favorite_numbers["coco"]))
print("Karen: " + str(favorite_numbers["karen"]))
print("Manuela: " + str(favorite_numbers["manuela"]))

for key, value in favorite_numbers.items():
    print("\nEl numero favorito de {} es:".format(key).title())
    print("{}".format(value))

glossary = {
    "BaaS": "Backup as a Service",
    "DRaaS": "Disaster Recovery as a Service",
    "SQL": "Database Engine",
    "EC2": "elastic Cloud Computing"
}

print("\nBaaS: " + str(glossary["BaaS"]))
print("DRaaS: " + str(glossary["DRaaS"]))
print("SQL: " + str(glossary["SQL"]))
print("S3: " + str(glossary["EC2"]))

for key, value in glossary.items():
    print("\nTermino: {}".format(key))
    print("{}".format(value))

print("\nFor KEYS")
for termino in glossary.keys():
    print(termino.upper() + ": " + glossary[termino])

cool_tech = ["EC2", "DRaaS"]

print("\nAccesing Keys for loops")
for termino in glossary:
    print(termino.upper())
    if termino in cool_tech:
        print("EN LISTA: La definicion del termino {} es: {}".format(termino, glossary[termino]))

print("\nBuscando en la lista el termino: IaaS")
if "IaaS" not in glossary:  # esto es el default de glossary.keys()
    print("Please add IaaS to the Glossary!")

print("\nSorting Lists")
for termino in sorted(glossary):
    print(termino)

print("\nVamos a obtener lista por VALUES, not KEYS")
favorite_colors = {
    "coco": "black",
    "ale": "blue",
    "karen": "pink",
    "isa": "pink"
}

for color in favorite_colors.values():
    print("\n{}".format(color))

print("\nLista por KEYS pero sin REPETIDOS")
print("En la lista anterior estaba repetido el color PINK. En esta lista ya no")
for color in set(favorite_colors.values()):
    print("\n{}".format(color))
