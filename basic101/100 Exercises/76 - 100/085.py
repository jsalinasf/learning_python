# Exercise 85

import os

file_item_path_raw = os.path.join(os.path.dirname(__file__), "countries_raw.txt")
file_item_path_filtered = os.path.join(os.path.dirname(__file__), "countries_filtered.txt")

countries_list_raw = open(file_item_path_raw, "r")
countries_list_filtered = open(file_item_path_filtered, "w")

countries_list_raw.readline()

for country in countries_list_raw:
  if (country == "\n"):
    continue
  if (country == "Top of Page\n"):
    continue
  if (country == "Top of Page"):
    continue
  if (len(country) < 3):
    continue
  countries_list_filtered.writelines(country)

countries_list_raw.close()
countries_list_filtered.close()