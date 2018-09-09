# Exercise 71

import requests

web_r = requests.get("http://www.pythonhow.com/data/universe.txt")

text = web_r.text

count_a = text.count("a")

print(count_a)