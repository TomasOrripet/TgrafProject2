from OpenGL.GL import *
from OpenGL.GLU import *

class bricks():

    def __init__(self, rows, Xsize, Ysize):
        self.__rows = rows
        self.__displayX = Xsize
        self.__displayY = Ysize 
        self.__sizeX = 18 
        self.__sizeY = 10
        self.__cols = Xsize//20
        self.__posX = 20
        self.__bricklist = []

        for i in range(self.__rows):
            for j in range(self.__cols):
                print(F"row: {i}\ncols: {j}")
        
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


