from OpenGL.GL import *
from OpenGL.GLU import *

class bricks():

    def __init__(self, posX, posY):
        self.__posX = posX
        self.__posY = posY
        self.__sizeX = 38
        self.__sizeY = 18
        pass

    def display(self):     
        
        glBegin(GL_QUADS)
        glVertex3f(self.__posX + self.__sizeX/2, self.__posY + self.__sizeY/2,0)
        glVertex3f(self.__posX + self.__sizeX/2, self.__posY - self.__sizeY/2,0)
        glVertex3f(self.__posX - self.__sizeX/2, self.__posY - self.__sizeY/2,0)
        glVertex3f(self.__posX - self.__sizeX/2, self.__posY + self.__sizeY/2,0)   
        glEnd()

    def x_ypos(self):
        return self.__posX , self.__posY


