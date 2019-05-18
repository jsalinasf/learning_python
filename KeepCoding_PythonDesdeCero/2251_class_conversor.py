class Termometro():
    
    def __str__(self):
        return '{}° {}'.format(self.__temperatura, self.__unidadM)
    
    def __init__(self):
        self.__temperatura = 0
        self.__unidadM = 'C'
    
    def conversor(self, __temperatura, unidad):
        if unidad == 'C':
            return "{}°F".format((__temperatura) * 9/5 + 32)
        elif unidad == 'F':
            return "{}°C".format((__temperatura - 32) * 5/9)
        else:
            'Unidad Incorrecta'
    
    # Setters and Getters
    def temp(self, value=None):
        if value == None:
            return self.__temperatura
        else:
            self.__temperatura = value
    
    def unidadMedida(self, value=None):
        if value == None:
            return self.__unidadM
        else:
            if value == 'C' or value == 'F':
                self.__unidadM = value
    
Termometro01 = Termometro()
print(Termometro01)
Termometro01.temp(25)
Termometro01.unidadMedida('C')
print(Termometro01)
print(Termometro01.conversor(Termometro01.temp(),Termometro01.unidadMedida()))
        


    