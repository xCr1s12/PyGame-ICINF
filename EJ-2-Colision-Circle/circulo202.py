import pygame
import math as mt

class Circulo2():
    def __init__(self, x , y, radius):
        self.x = x
        self.y = y
        self.color = (219,112,147)
        self.velocity = 0.1
        self.radius = radius

    def draw(self, screen):
        circle = (self.x ,self.y)
        pygame.draw.circle(screen , self.color , circle, self.radius)

    def move(self, key):
        self.ex = 0
        self.ey = 0
        if key[pygame.K_s]:
            self.ey += self.velocity
        if key[pygame.K_w]:
            self.ey -= self.velocity
        if key[pygame.K_a]:
            self.ex -= self.velocity
        if key[pygame.K_d]:
            self.ex += self.velocity
        
        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2)
        
        self.x += self.ex
        self.y += self.ey
    


    
    def posicion(self):
        return [self.x, self.y]

 

 
