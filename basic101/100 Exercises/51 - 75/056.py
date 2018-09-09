# Exercise 56
import json
import os

file_item_path = os.path.join(os.path.dirname(__file__), "056.json")

d = {
  "employees":[{"firstName": "John", "lastName": "Doe"}, {"firstName": "Anna", "lastName": "Smith"},                    {"firstName": "Peter", "lastName": "Jones"}], 
  "owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy","lastName": "Petter"}]
  }

print(d["employees"])

with open(file_item_path, "w") as fp:
  json.dump(d, fp, indent=4, sort_keys=True)

