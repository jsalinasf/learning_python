class Termometro():
    
    def __str__(self):
        return '{}° {}'.format(self.__temperatura, self.__unidadM)
    
    # Constructor
    def __init__(self):
        self.__temperatura = 0
        self.__unidadM = 'C'
    
    def __conversor(self, __temperatura, unidad):
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
    
    def mide(self, unidadMedida = None):
        if unidadMedida == None or unidadMedida == self.__unidadM:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidadM)
    
Termometro01 = Termometro()
print(Termometro01)
Termometro01.temp(32)
Termometro01.unidadMedida('F')
print(Termometro01)
print(Termometro01.mide('C'))
        


    