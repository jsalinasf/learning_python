# Exercise 57
import json
import os
from pprint import pprint

file_item_path = os.path.join(os.path.dirname(__file__), "056.json")

with open(file_item_path, "r") as fp:
  d = json.loads(fp.read())

pprint(d)
