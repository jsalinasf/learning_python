# Exercise 58
import json
import os
from pprint import pprint

file_item_path = os.path.join(os.path.dirname(__file__), "056.json")

with open(file_item_path, "r+") as fp:
  d = json.loads(fp.read())

  pprint(d)

  d["employees"].append( {"firstName": "Jorge", "lastName": "Salinas"} )

  fp.seek(0)  # Manda el cursor al inicio del archivo y pone el nuevo diccionario
  
  json.dump(d, fp, indent=4, sort_keys=True)

  fp.truncate() # borra el contenido que tenia antes porque quedo debajo del nuevo diccionario.

