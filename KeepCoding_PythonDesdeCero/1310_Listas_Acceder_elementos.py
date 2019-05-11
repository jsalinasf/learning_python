daysOfTheMonth = (31,28,31,30,31,30,31,31,30,31,30,31)

print(len(daysOfTheMonth))
print(max(daysOfTheMonth))
print(min(daysOfTheMonth))
print(daysOfTheMonth[2])

print(daysOfTheMonth[5:9])
print(daysOfTheMonth[9:])
print(daysOfTheMonth[:5])

a = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dec']

# Solo copia la referencia (direccion de memoria), pero la lista es la misma
# Esto aplica solo para tipos de datos complejos
# Esto NO aplica para tipos de datos simples como Enteros, Float, etc.
# Esto se llama PASO POR REFERENCIA 
b = a

# Si quiero clonar el contenido a una nueva lista debo hacer:
c = a[:]

print(a)
print(b)
a.append('Juliembre')
print(a)
print(b)
print(c)

# Rangos Negativos
print(c[-1])
print(c[-5:-1])
print(c[-5:])


# Remove ultimo elemento
c.pop()
print(c)

a = 0.1
b = 0.2
c = a + b
print(c)