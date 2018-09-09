films = {
    "Bourne":[18,5],
    "Ghosts Busters":[12,5],
    "Finding Dory":[3,5]
    }

while True:

    choice = input("What Film would you like to watch?: ").strip().title()

    
    if choice in films:
        age = int(input("How old are You?: ").strip())

        #Check User Age
        if age >= films[choice][0]:

            #Check Enough Seats
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("sorry, we are sould out!")
        
        else:
            print("You are too young to see this movie")
    else:
        print("I'm sorry but We don't have that film....")      

        
