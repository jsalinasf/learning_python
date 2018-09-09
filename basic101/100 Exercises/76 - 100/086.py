# Exercise 086

import os

file_item_path = os.path.join(os.path.dirname(__file__), "countries_clean.txt")
content = open(file_item_path, "r")
content.readline()

checklist = ["Portugal", "Germany", "Munster", "Spain", "Ecuador"]

content = [i.strip("\n") for i in content if "\n" in i]

content = [country for country in checklist if country in content]

print(content)



