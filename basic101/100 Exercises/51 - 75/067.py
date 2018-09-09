# Exercise 67

def translate (d, searchWord):
  # if searchWord in d:
  #   return d[searchWord]
  # else:
  #   return("The word doesnt exist")
  try:
    return d[searchWord]
  except KeyError:
    return("The word doesnt exist")


d = dict(weather = "clima", earth = "terra", rain = "chuva")
inputWord = input("Enter word: ")
print(translate(d, inputWord))
