# Exercise 8.15 Importing Functions and models

import mis_funciones as coco
from mis_funciones import print_models
from mis_funciones import show_completed_models as ale

unprinted_designs = ["iphone case", "robot pendant", "picture frame"]
completed_models = []

print(unprinted_designs)
print(completed_models)

print_models(unprinted_designs, completed_models)  # La llamo directamente
ale(completed_models)  # La llamo utilizando el alias especifico para la funcion
coco.show_completed_models(completed_models)  # la llamo utilizando el alias del modulo

print(unprinted_designs)
print(completed_models)
