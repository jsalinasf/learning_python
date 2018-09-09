from random import choice

questions = ["Why is the sky blue?: ",
             "How tall are buildings?: ",
             "why do planes fly?: "
             ]

pregunta = choice(questions)

answer = input(pregunta).strip().lower()

while answer != "just because":
    answer = input ("Why?: ").strip().lower()

print ("Oh... Okay")
 
