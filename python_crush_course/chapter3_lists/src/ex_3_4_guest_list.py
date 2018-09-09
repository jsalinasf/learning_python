# Exercise 3.4 - Lists

guests = ["Jesus", "Jim Morrison", "Ghandi"]

print("Hi Mr. " + guests[0] + ", you are invited for dinner")
print("Hi Mr. " + guests[1] + ", you are invited for dinner")
print("Hi Mr. " + guests[2] + ", you are invited for dinner")

guests[1] = "Marilyn Monroe"

print("\nHi Mr. " + guests[0] + ", you are invited for dinner")
print("Hi Mr. " + guests[1] + ", you are invited for dinner")
print("Hi Mr. " + guests[2] + ", you are invited for dinner")

print("\nI found a bigger dinner Table, new guests will arrive!")

guests.insert(0, "Malcon X")
guests.insert(2, "Adolf Hitler")
guests.append("Napoleon Bonaparte")

print("\nHi Mr. " + guests[0] + ", you are invited for dinner")
print("Hi Mr. " + guests[1] + ", you are invited for dinner")
print("Hi Mr. " + guests[2] + ", you are invited for dinner")
print("Hi Mr. " + guests[3] + ", you are invited for dinner")
print("Hi Mr. " + guests[4] + ", you are invited for dinner")
print("Hi Mr. " + guests[5] + ", you are invited for dinner")

print("\nTenemos la siguiente cantidad de invitados: " + str(len(guests)))

print("\nVamos ordenar la lista - SORT 'PERMANENTE':")
print(guests)
guests.sort()
print(guests)

print("\nVamos a reversar la lista - OJO LA LISTA QUE FUE HECHO SORT:")
print(guests)
guests.reverse()
print(guests)

print("\nSorry.... the bigger table wont arrive on Time I will have to shorten the guests lists")
print(guests)
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print("\nHi Mr. " + guests[0] + ", you are STILL invited for dinner")
print("Hi Mr. " + guests[1] + ", you are STILL invited for dinner")

guests.remove("Napoleon Bonaparte")
del guests[0]

print(guests)






