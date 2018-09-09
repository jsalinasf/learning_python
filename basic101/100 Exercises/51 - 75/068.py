# Exercise 068
import platform

def translate (d, searchWord):
  try:
    return d[searchWord]
  except KeyError:
    return ("The word doesnt exist")


d = dict(weather = "clima", earth = "terra", rain = "chuva")
inputWord = input("Enter world: ").lower()
print(translate(d, inputWord))
print("Python Version: {}".format(platform.python_version()))