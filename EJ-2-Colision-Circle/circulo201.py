import pygame
import math as mt

class Circulo():
    def __init__(self, x , y, radius):
        self.x = x
        self.y = y
        self.color = (192,192,192)
        self.velocity = 0.2
        self.radius = radius

    def draw(self, screen):
        circle = (self.x ,self.y)
        pygame.draw.circle(screen , self.color , circle, self.radius)

    def move(self, key):
        self.ex = 0
        self.ey = 0
        if key[pygame.K_DOWN]:
            self.ey += self.velocity
        if key[pygame.K_UP]:
            self.ey -= self.velocity
        if key[pygame.K_LEFT]:
            self.ex -= self.velocity
        if key[pygame.K_RIGHT]:
            self.ex += self.velocity
        
        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2)
        
        self.x += self.ex
        self.y += self.ey
    
    

    
    def posicion(self):
        return [self.x, self.y]    


 
