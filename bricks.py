from OpenGL.GL import *
from OpenGL.GLU import *

class bricks():

    def __init__(self, rows, Xsize, Ysize):
        pass

    def display(self):
        for row in range(self.__rows):
            for col in range(self.__cols):
                glBegin(GL_QUADS)
                glVertex3f(self.__posX * col + self.__sizeX, 
                            self.__displayY-(self.__sizeY * row) - self.__sizeY+2,0)
                glVertex3f(self.__posX * col + self.__sizeX,
                            self.__displayY-(self.__sizeY * row),0)
                glVertex3f(self.__posX * col , 
                            self.__displayY-(self.__sizeY * row), 0)
                glVertex3f(self.__posX * col, 
                            self.__displayY-(self.__sizeY * row) - self.__sizeY+2,0)
                glEnd()


