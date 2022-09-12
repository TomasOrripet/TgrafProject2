import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from random import *
import math


class Ball:

    def __init__(self,velocity):
        self.amount_of_triangles = 20
        self.radius = 10
        self.x_pos = 380
        self.y_pos = 100
        self.velocity = [4,8]




    
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
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]


    def check_if_ball_hits_wall(self):
        
        if self.x_pos >= 790:
            self.velocity[0]  = - self.velocity[0]
        if self.x_pos <= 0:
            self.velocity[0]  = - self.velocity[0]
        if self.y_pos >= 590:
            self.velocity[1]  = - self.velocity[1]
        if self.y_pos <= 0:
            self.velocity[1]  = - self.velocity[1]