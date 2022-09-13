import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from random import *
from paddle import paddle
from bricks import bricks
from ball import Ball





class Breakout:
        
    def __init__(self):
        self.__displayX = 600
        self.__displayY = 800
        self.__level = 1
        self.__brickList = []
        pygame.display.init()
        pygame.display.set_mode((self.__displayX, self.__displayY), DOUBLEBUF|OPENGL) #800 pixels wide and 600 pixels high
        
        self.__Paddle = paddle(self.__displayX)
        self.createBricks()
        
        glClearColor(0.0, 0.0, 0.0, 1.0)
        
        self.__Ball = Ball()
        self.clock = pygame.time.Clock()

    def createBricks(self):
        sizeY = 20
        sizeX = 40
        for i in range(self.__level):
            posY = self.__displayY - (sizeY * i) - 10
            for j in range (15):
                    posX = sizeX * j + 20
                    self.__brickList.append(bricks(posX, posY))
                    
        

    def update(self):
        self.__Paddle.update()

        self.__Ball.update()
        self.__Ball.check_if_ball_hits_wall()
        
        self.__Ball.check_paddle(self.__Paddle.xpos())
        

        self.__brickList = self.__Ball.check_bricks(self.__brickList)
        
        if (len(self.__brickList) == 0):
            self.__level += 1
            self.__Ball = Ball()
            self.createBricks()


        
        
        pass
            


    def display(self):

        
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, self.__displayX, self.__displayY)
        gluOrtho2D(0, self.__displayX, 0, self.__displayY)
        

        
        #the paddle
        self.__Paddle.display()
        #self.__Bricks.display()
        self.__Ball.display()
        for brick in self.__brickList:
            brick.display()

        


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
                    elif event.key == K_r:
                        self.__level = 1
                        self.__Ball = Ball()
                        self.__brickList = []
                        self.createBricks()
                elif event.type == pygame.KEYUP:
                    if event.key == K_LEFT:
                        self.__Paddle.lStop()
                    if event.key == K_RIGHT:
                        self.__Paddle.rStop()
                        pass
        self.clock.tick(60)
        self.update()
        self.display()

if __name__ == "__main__":
    breakout = Breakout()
    while True:
        breakout.game_loop()





