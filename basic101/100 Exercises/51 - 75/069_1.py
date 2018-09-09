# Exercise 069
import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])