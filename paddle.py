from OpenGL.GL import *
from OpenGL.GLU import *


going_right = False
going_left = False

class paddle():



    def __init__(self, Xsize) -> None:
        self.__posX = 280
        self.__posY = 50
        self.__sizeX = 80
        self.__sizeY = 10
        self.__goLeft = False
        self.__goRight = False
        self.__xMax = Xsize - self.__sizeX
        self.__xMin = 80
        self.__speed = 2
        self.__velocity = 1

    def display(self):
        glBegin(GL_QUADS)

        glVertex3f(self.__posX + self.__sizeX, self.__posY + self.__sizeY,0)
        glVertex3f(self.__posX + self.__sizeX, self.__posY - self.__sizeY,0)
        glVertex3f(self.__posX - self.__sizeX, self.__posY - self.__sizeY,0)
        glVertex3f(self.__posX - self.__sizeX, self.__posY + self.__sizeY,0)

        glEnd()

    def xpos(self):
        return self.__posX

    def left(self):
        self.__goLeft = True
    
    def right(self):
        self.__goRight = True

    def lStop(self):
        self.__goLeft = False

    def rStop(self):
        self.__goRight = False

    def update(self):
        self.__velocity *= 1.1

        if self.__velocity > 4:
            self.__velocity = 4

        if((self.__goLeft and self.__goRight)or(not self.__goLeft and not self.__goRight)):
            self.__velocity = 1        
        if self.__goLeft:
            self.__posX -= self.__speed * self.__velocity
        if self.__goRight:
            self.__posX += self.__speed * self.__velocity

        if self.__posX > self.__xMax:
            self.__posX = self.__xMax
        if self.__posX < self.__xMin:
            self.__posX = self.__xMin

