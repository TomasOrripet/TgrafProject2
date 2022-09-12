from operator import truediv
from OpenGL.GL import *
from OpenGL.GLU import *


going_right = False
going_left = False

class paddle:

    def __init__(self, Xsize, Ysize) -> None:
        self.__posX = 280
        self.__posY = 50
        self.__sizeX = 80
        self.__sizeY = 10
        self.__goLeft = False
        self.__goRight = False
        self.__xMax = Xsize - self.__sizeX
        self.__xMin = 0

    def display(self):
        glBegin(GL_QUADS)
        glVertex3f(self.__posX + self.__sizeX, self.__posY + self.__sizeY,0)
        glVertex3f(self.__posX + self.__sizeX, self.__posY - self.__sizeY,0)
        glVertex3f(self.__posX - self.__sizeX, self.__posY - self.__sizeY,0)
        glVertex3f(self.__posX - self.__sizeX, self.__posY + self.__sizeY,0)
        glEnd()

    def left(self):
        self.__goLeft = True
    
    def right(self):
        self.__goRight = True

    def lStop(self):
        self.__goLeft = False

    def rStop(self):
        self.__goRight = False

    def update(self):
        if self.__goLeft:
            self.__posX -= 0.1
        if self.__goRight:
            self.__posX += 0.1

