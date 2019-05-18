class Dog():        
    def __str__(self):
        return 'I\'m {} the Dog'.format(self.name)
    
    # Object Constructor
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        if self.weight > 8:
            print('GUAUU... GUAUU')
        else:
            print('Guauuu... Guauuu')

class AsistantDog(Dog):
    # Overwritten a method - This methos exists in the father class but it is being overwritten 
    def __str__(self):
        return 'I\'m an Assistant Dog {} for {}'.format(self.name, self.master)
    
    # Object Constructor
    def __init__(self, name, age, weight, master):
        # Cuando invoco la clase Padre debo pasar esta instancia 'self'
        Dog.__init__(self, name, age, weight)
        self.master = master
        self.__isWorking = True
    
    def takeWalk(self, partOfDay):
        print('I help my Master {} to walk in the {}'.format(self.master, partOfDay))
    
    def bark(self):
        if self.__isWorking:
            print('Shhh I can\'t bark')
        else:
            Dog.bark(self)
    
    # SETTER & GETTER
    def working(self, value=None):
        if value == None:
            return self.__isWorking
        else:
            self.__isWorking = value


Sara = Dog('Sara', 4, 27)
print(Sara.name)
print(Sara.age)
print(Sara.weight)
Sara.bark()
print(Sara)

Sheyla = Dog('Sheyla',2,5)
print(Sheyla.name)
print(Sheyla.age)
print(Sheyla.weight)
Sheyla.bark()

Can09 = AsistantDog('Can09',5,21,'Mike Perez')
print(Can09.name)
print(Can09.age)
print(Can09.weight)
print(Can09.master)
Can09.bark()
print(Can09.working())
Can09.working(False)
print(Can09.working())
Can09.bark()
Can09.takeWalk('evening')
print(Can09)
