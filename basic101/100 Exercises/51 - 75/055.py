# Exercise 55

d = {
  "employees":[{"firstName": "John", "lastName": "Doe"}, {"firstName": "Anna", "lastName": "Smith"},                    {"firstName": "Peter", "lastName": "Jones"}], 
  "owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy","lastName": "Petter"}]
  }

print(d["employees"])

d["employees"].append( {"firstName": "Jorge", "lastName": "Salinas"} )

print(d["employees"])
