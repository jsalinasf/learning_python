import pygame, sys
from pygame.locals import *

class Termomentro():
    def __init__(self):
        self.custome = pygame.image.load('images/termo1.png')
    
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else :
            resultado = grados
        
        return '{:10.2f}'.format(resultado)


class NumberInput():
    __value = 0
    __strValue = ''
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0

    def __init__(self, value=0):
        self.__font = pygame.font.SysFont('Arial', 24)
        self.value(value)
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0):
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                if self.__strValue[:-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1]
                self.value(self.__strValue)

    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size

        return (rect, textBlock)

    # Getters and Setters
    def value(self, value=None):
        if value == None:
            return self.__value
        else:
            value = str(value)
            try:
                self.__value = float(value)
                self.__strValue = value
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass

    def width(self, value=None):
        if value == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(Value)
            except:
                pass
    
    def height(self, value=None):
        if value == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(Value)
            except:
                pass
    
    def size(self, value=None):
        if value == None:
            return self.__size
        else:
            try:
                w = int(value[0])
                h = int(value[1])
                self.__size = [w, h]
            except:
                pass
    
    def posX(self, value=None):
        if value == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(Value)
            except:
                pass
    
    def posY(self, value=None):
        if value == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(Value)
            except:
                pass
    
    def pos(self, value=None):
        if value == None:
            return self.__position
        else:
            try:
                self.__position = [int(value[0]), int(value[1])]
            except:
                pass

class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad='C'):
        self.__customes = []
        self.__customes.append(pygame.image.load('images/posiF.png'))
        self.__customes.append(pygame.image.load('images/posiC.png'))
        self.__tipoUnidad = unidad
    
    def custome(self):
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def change(self):
        if self.__tipoUnidad =='F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
    
    def unidad(self):
        return self.__tipoUnidad


class mainApp():
    termometro = None
    entrada = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption('Termometro')
        self.__screen.fill((244, 236, 203))
        self.termometro = Termomentro()
        self.entrada = NumberInput('')
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        self.selector = Selector()
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        exitApp = False
        while not exitApp:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exitApp = True
                    self.__on_close
                
                self.entrada.on_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)


            # Pintamos el fondo de pantalla(background)
            self.__screen.fill((244, 236, 203))

            
            # Pintanmos el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            # Pintamos el cuadro de Texto
            text = self.entrada.render() # Obtenemos rectangulo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # Creamos el rectangulo blanco con sus datos (posicion y tamano)
            self.__screen.blit(text[1], self.entrada.pos()) # Creamos la foto de Texto 

            # Pintamos Selector
            self.__screen.blit(self.selector.custome(), (112, 153))

            # Actualizar Pantalla
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
