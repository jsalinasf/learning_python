import pygame, sys, random

class Runner():

    __customes = ('turtle', 'fish', 'octupus')
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0,2)
        self.custome = pygame.image.load('images/{}.png'.format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ''
    
    def avanzar(self):
        self.position[0] += random.randint(1,3)


class Game():
    
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Flash')
    __startLine = 0
    __finishLine = 620

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Run little Turtle... Run!')
        self.background = pygame.image.load('images/background.png')
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)    

    def competir(self):
        gameOver = False
        while not gameOver:
            # comprobar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True          
            
            for runner in self.runners:
                runner.avanzar()
                # Comprobar si hay ganador
                if runner.position[0] >= self.__finishLine:
                    gameOver = True
                    print('{} ha gando!'.format(runner.name))

            # Actualizar Objetos
            self.__screen.blit(self.background, (0, 0))
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            # Presentar Pantalla con objetos actualizados
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
