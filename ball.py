import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from random import *
import math


class Ball:

    def __init__(self):
        self.amount_of_triangles = 20
        self.radius = 10
        self.x_pos = 380
        self.y_pos = 100
        self.velocity = [4,8] #einhverjar random tölur




    
    def display(self):

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x_pos,self.y_pos)
        for i in range(self.amount_of_triangles):
            glVertex2f(
            self.x_pos + (self.radius * math.cos(i*(2*self.radius)//self.amount_of_triangles)),
            self.y_pos + (self.radius * math.sin(i*(2*self.radius)//self.amount_of_triangles))
            )

        glEnd()

    def update(self):
        self.x_pos += 4
        self.y_pos += 4


    def ball_check(self):
        #we check if the ball is bouncing against any of the 4 walls
        if self.x_pos > 780:
            self.x_pos -= self.x_pos

        if self.x_pos <= 0:
            self.x_pos -= self.x_pos
        if self.y_pos >= 580:
            self.y_pos -= self.y_pos
        if self.y_pos <= 0:
            self.y_pos -= self.y_pos




