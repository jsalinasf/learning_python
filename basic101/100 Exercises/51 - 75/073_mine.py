# Exercise 73
import os
import requests

url = "http://www.pythonhow.com/data/sampledata.txt"

web_r = requests.get(url)

text = (web_r.text).split("\n")
print(text)

filepath = os.path.join(os.getcwd(), "basic101/100 Exercises/51 - 75", "073_mine.txt")

with open(filepath, "w") as output_file:
  for line in text:
    if "x,y" in line:
      output_file.write(line + "\n")
    else:
      new_line = ""
      for character in line:
        if character.isdigit():
          character = int(character) * 2
          new_line += str(character)
        else:
          new_line += character
      output_file.write(new_line + "\n")

output_file.close()
