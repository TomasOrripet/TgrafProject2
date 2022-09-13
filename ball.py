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
        self.x_pos = 70#380
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
        if self.x_pos >= 590:
            self.velocity[0]  = - self.velocity[0]
        if self.x_pos <= 0:
            self.velocity[0]  = - self.velocity[0]
        if self.y_pos >= 790:
            self.velocity[1]  = - self.velocity[1]
        if self.y_pos <= 0:
            #self.velocity[1]  = - self.velocity[1]
            pass

        
    

    def check_paddle(self, paddleX):
        if self.y_pos < 60 and self.y_pos > 50:
            if self.x_pos < paddleX  and self.x_pos > paddleX -60 :
                frommid = paddleX - self.x_pos
                self.velocity[1] = - self.velocity[1]
                self.velocity[0] = - frommid/10
            if self.x_pos > paddleX and self.x_pos < paddleX + 60:
                frommid = self.x_pos - paddleX 
                self.velocity[0] = + frommid/10
                self.velocity[1] = - self.velocity[1]

        pass

    def check_bricks(self, bricks):
        if self.y_pos > 720:
            for brick in bricks:
                x,y = brick.x_ypos()
            
                #top top
                #botom botm
                #left left
                #right right

                ballright = self.x_pos +10
                ballleft = self.x_pos - 10
                brickright = x+19
                brickleft = x-19
                ballTop = self.y_pos + 10
                ballbottom = self.y_pos -10
                brickBottom = y - 9
                bricktopp = self.y_pos + 9
                
                if self.velocity[1]>0:
                #topBall bottom brick collison
                    
                    
                    
                    if ballTop > brickBottom:

                        if self.velocity[0]>0:
                            #rightball leftbrick
                            if ballright > brickleft and ballright < brickright:
                                inx = (ballright - brickleft)
                                iny = ballTop - brickBottom
                                if (iny <= inx):
                                    self.velocity[1] = -self.velocity[1]
                                    bricks.remove(brick)
                                    print("down")
                                else:
                                    self.velocity[0] = -self.velocity[0]
                                    bricks.remove(brick)
                                    print("left")
                                print("ball top -> right")
                                print(F"in x: {inx}")
                                print(F"in y: {iny}")
                                
                        
                        else:
                            #leftball rightbrick
                            if ballleft < brickright and ballleft > brickleft:
                                inx = (brickright - ballleft)
                                iny = ballTop - brickBottom
                                if (iny <= inx):
                                    self.velocity[1] = -self.velocity[1]
                                    bricks.remove(brick)
                                    print("down")
                                else:
                                    print("right")
                                    self.velocity[0] = -self.velocity[0]
                                    bricks.remove(brick)
                                print("ball top -> left")
                                print(F"in x: {inx}")
                                print(F"in y: {iny}")
                                
                else:
                    if ballbottom < bricktopp and ballbottom > brickBottom :

                        if self.velocity[0]>0:
                            #rightball leftbrick
                            if ballright > brickleft and ballright < brickright:
                                inx = ballright - brickleft
                                iny = bricktopp - ballbottom
                                if iny <= inx:
                                    self.velocity[1] = -self.velocity[1]
                                    print("down")
                                    bricks.remove(brick)
                                else:
                                    self.velocity[0] = -self.velocity[0]
                                    print("left")
                                    bricks.remove(brick)
                                print("ball bottom -> right")
                                print(F"in x: {inx}")
                                print(F"in y: {iny}")
                                

                        else:
                            #leftball rightbrick
                            if ballleft < brickright and ballleft > brickleft:
                                inx = (brickright - ballleft)
                                iny = bricktopp - ballbottom
                                if (iny <= inx):
                                    self.velocity[1] = -self.velocity[1]
                                    print("down")
                                    bricks.remove(brick)
                                else:
                                    print("right")
                                    self.velocity[0] = -self.velocity[0]
                                    bricks.remove(brick)
                                print("ball bottom -> left")
                                print(F"in x: {inx}")
                                print(F"in y: {iny}")

                            



                    
                 
                    

                        
                        
                        

                        #print(F"X: {x}\nY: {y}\nSX: {self.x_pos}\nSY: {self.y_pos}")
                        #self.velocity[1] = - self.velocity[1]


                #if (self.y_pos + 10 < y and self.y_pos -10 < y + 18) and (self.x_pos > x and self.x_pos < x+38 ):
                #    print(F"X: {x}\nY: {y}\nSX: {self.x_pos}\nSY: {self.y_pos}")
                #    self.velocity[1] = - self.velocity[1]

            
                                                      
                        




                    
        return bricks



        
        pass
