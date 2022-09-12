import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from random import *
from paddle import paddle






class Breakout:
        
    def init_game(self):
        
        pygame.display.init()
        pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL) #800 pixels wide and 600 pixels high
        self.__Paddle = paddle()
        
        glClearColor(0.0, 0.0, 0.0, 1.0)


    def update(self):
        pass
            


    def display(self):

        
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, 800, 600)
        gluOrtho2D(0, 800, 0, 600)

        #the paddle
        self.__Paddle.display()

        


        pygame.display.flip()

    def game_loop(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == K_q:
                        glClearColor(random(), random(), random(), 1.0)
                    elif event.key == K_LEFT:
                        self.__Paddle.left()
                    elif event.key == K_RIGHT:
                        self.__Paddle.right()
                elif event.type == pygame.KEYUP:
                    if event.key == K_LEFT:
                        pass
                    if event.key == K_RIGHT:
                        pass
                
        #update()
        self.display()

if __name__ == "__main__":
    breakout = Breakout()
    breakout.init_game()
    while True:
        breakout.game_loop()





