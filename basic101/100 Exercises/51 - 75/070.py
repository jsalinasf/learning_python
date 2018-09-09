# Exercise 70

import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
print(text)
