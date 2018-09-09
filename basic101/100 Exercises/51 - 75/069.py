# Exercise 69

import os

file_item_path = os.path.join(os.path.dirname(__file__), "069_1.py")

print(file_item_path)

with open(file_item_path, "w") as pyFile:
  pyFile.write("# Exercise 069")
  pyFile.write("\nimport requests\n\n")
  pyFile.write('r = requests.get("http://www.pythonhow.com")')
  pyFile.write("\nprint(r.text[:100])")
  pyFile.close()
