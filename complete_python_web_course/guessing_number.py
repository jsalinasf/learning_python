# This program put the user to guess the number in a selected range

import random

def evalua_intento(num1,numero_pensando):
    if num1 == numero_pensando:
        return True
    else:
        return False

def pista_usuario(num1,numero_pensando):
    if num1 < numero_pensando:
        print("Y si probramos con un numero mayor?")
    else:
        print("Yo probaria con un numero menor ;)")
        

print("Adivina Adivinador")
tope = int(input("Ingrese un numero: "))
print("Vamos a adivinar un numero entre 1 y {}, ok?".format(str(tope)))

keep_playing = "s"

numero_pensando = random.randint(1,tope+1)
#print(str(numero_pensando))
cont = 1

while keep_playing != "n":
    print("Intento {}:".format(cont))
    intento = int(input("Que numero estoy pensando?: "))

    if (intento > 0 and intento <= tope):
        
        if evalua_intento(intento,numero_pensando):
            print("Felicitaciones... {} es el numero que habia pensando!".format(intento))
            print("Le tomo {} intentos adivinar!".format(cont))
            break
        else:
            pista_usuario(intento,numero_pensando)
            keep_playing = input("Desea seguir intentando (s/n)?: ").strip().lower()

        if keep_playing == "n":
            keep_playing == "n"
            print("El numero era {}.... Gracias por intentar :)".format(numero_pensando))
        cont +=1

    else:
        print("Numero fuera de rango, vuelva a intentar")
