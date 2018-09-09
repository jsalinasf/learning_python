# Exercise 066

def translate (dict, searchWord):
  return dict[searchWord]



d = dict(weather = "clima", earth = "terra", rain = "chuva")
word = input("Enter world: ")
print(translate(d, word))
