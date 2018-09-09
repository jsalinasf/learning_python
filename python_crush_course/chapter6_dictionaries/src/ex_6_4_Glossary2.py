# Exercises 6.4 to 6.6

glossary = {
    "BaaS": "Backup as a Service",
    "DRaaS": "Disaster Recovery as a Service",
    "SQL": "Database Engine",
    "EC2": "Elastic Cloud Computing",
    "IaaS": "Infrastructure as a Service",
    "AD": "Active Directory Services"
}

for term in glossary:
    print(term)

biggest_rivers = {
    "nile": "egypt",
    "amazonas": "brasil",
    "missisipi": "usa",
    "yellow": "china"
}

for river in biggest_rivers:
    print("The " + river.title() + " runs through " + biggest_rivers[river].title())

print("\nPrinting RIVERS:")
for river in biggest_rivers:
    print(river.title())

print("\nPrinting COUNTRIES:")
for country in biggest_rivers.values():
    print(country.title())

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
print("\nLanguages Poll")
take_poll = ["jen", "sarah", "jorge", "karen", "phil", "isa"]
for respondant in take_poll:
    if respondant in favorite_languages:
        print("{}, thank you for taking the poll".format(respondant).title())
    else:
        print("{}, please take the poll".format(respondant).title())
