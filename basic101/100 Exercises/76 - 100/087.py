
# import os
# cwd = os.getcwd()
# print(cwd)

checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open ("basic101\\100 Exercises\\76 - 100\\countries_missing.txt", "r") as file:
  content = file.readlines()

for country in content:
  print(country)

updated_list = sorted(checklist + content)

with open("basic101\\100 Exercises\\76 - 100\\countries_missing_fixed.txt", "w") as file:
  for i in updated_list:
    file.write(i)
