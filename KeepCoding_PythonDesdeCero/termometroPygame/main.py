import pygame, sys
from pygame.locals import *

class Termomentro():
    def __init__(self):
        self.custome = pygame.image.load('images/termo1.png')

class mainApp():
    termometro = None
    entrada = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption('Termometro')
        self.__screen.fill((244, 236, 203))
        self.termometro = Termomentro()
    
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
            
            self.__screen.blit(self.termometro.custome, (50, 34))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()
