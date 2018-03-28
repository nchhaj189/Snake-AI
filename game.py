from pygame.locals import *
import pygame

class Snake:
    x = 20
    y = 20
    velocity = 10

    def L(self):
        self.x -= self.velocity
    def R(self):
        self.x += self.velocity
    def D(self):
        self.y += self.velocity
    def U(self):
        self.y -= self.velocity

class Game:

    windowWidth = 1000
    windowHeight = 800
    snake = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.snake = Snake()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.snake.x,self.snake.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.snake.R()

            if (keys[K_LEFT]):
                self.snake.L()

            if (keys[K_UP]):
                self.snake.U()

            if (keys[K_DOWN]):
                self.snake.D()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    game = Game()
    game.on_execute()
