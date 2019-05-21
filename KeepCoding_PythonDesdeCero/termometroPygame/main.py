import pygame, sys
from pygame.locals import *

class Termomentro():
    def __init__(self):
        self.custome = pygame.image.load('images/termo1.png')

class NumberInput():
    __value = 0
    __strValue = '0'
    __position = [0, 0]
    __size = [0, 0]

    def __init__(self, value=0):
        self.__font = pygame.font.SysFont('Arial', 24)
        self.value(value)
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10:
                self.__strValue += event.unicode
                self.value(self.__strValue)
            elif event.key == K_BACKSPACE:
                self.__strValue = self.__strValue[:-1]
                self.value =(self.__strValue)

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
                self.__value = int(value)
                self.__strValue = value
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


class mainApp():
    termometro = None
    entrada = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption('Termometro')
        self.__screen.fill((244, 236, 203))
        self.termometro = Termomentro()
        self.entrada = NumberInput(0)
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
    
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

            
            # Pintanmos el termometro en su posicion
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            # Pintamos el cuadro de Texto
            text = self.entrada.render() # Obtenemos rectangulo blanco y foto de texto y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) # Creamos el rectangulo blanco con sus datos (posicion y tamano)
            self.__screen.blit(text[1], self.entrada.pos()) # Creamos la foto de Texto 
            
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
