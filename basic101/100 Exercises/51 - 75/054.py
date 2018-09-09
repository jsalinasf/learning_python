# Exercise 54

d = {
  "employees":[{"firstName": "John", "lastName": "Doe"}, {"firstName": "Anna", "lastName": "Smith"},                    {"firstName": "Peter", "lastName": "Jones"}], 
  "owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy","lastName": "Petter"}]
  }

print(d["employees"])
print(d["employees"][1]["lastName"])
d["employees"][1]["lastName"] = "Smooth"
print(d["employees"][1]["lastName"])
print(d["employees"])
