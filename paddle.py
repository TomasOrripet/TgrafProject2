from OpenGL.GL import *
from OpenGL.GLU import *


going_right = False
going_left = False

class paddle:

    def __init__(self) -> None:
        self.__posX = 380
        self.__posY = 50
        self.__sizex = 80
        self.__sizey = 10

    def display(self):
        glBegin(GL_QUADS)
        glVertex3f(self.__posX + self.__sizex, self.__posY + self.__sizey,0)
        glVertex3f(self.__posX + self.__sizex, self.__posY - self.__sizey,0)
        glVertex3f(self.__posX - self.__sizex, self.__posY - self.__sizey,0)
        glVertex3f(self.__posX - self.__sizex, self.__posY + self.__sizey,0)
        glEnd()

    def left(self):
        self.__posX -= 0.5
    
    def right(self):
        self.__posX += 0.5

    def update():
        pass

