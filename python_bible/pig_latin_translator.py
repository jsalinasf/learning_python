
# Ask User for a sentence to convert

original = input("Please insert a sentence to convert: ").strip().lower()

# Split sentence into words

lista_palabras = original.split(" ")

# loop trought the words and convert to pig latin

vocales = ("a","e","i","o","u")
palabras_traducidas = []
aux1 = ""
aux2 = ""
conversion = ""

# Rules for Conversion
# If starts with a vowel, just add "yay" at the end of the word
# Otherwise, move the first consonant cluster to end, and add "ay"

for palabra in lista_palabras:

    # Starts with a vowel
    if palabra.startswith(vocales):
        palabras_traducidas.append(palabra + "yay")
    # Starts with consonant
    else:
        for letras in palabra:
            if letras in vocales:
                aux1 = palabra[:palabra.index(letras)]
                aux2 = palabra[palabra.index(letras):]
                conversion = aux2 + aux1 + "ay"
                palabras_traducidas.append(conversion)
                break

# stick words back together

mensaje_final = " ".join(palabras_traducidas)

# output final string

print("Pig Translation: " + mensaje_final)
