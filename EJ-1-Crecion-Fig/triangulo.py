import pygame
import math as mt


class Triangulo():
    def __init__(self, x ,y):
        self.x = x
        self.y = y 
        self.color = "red"
        self.velocidad = 0.5
        
    def dibujarT(self,screen):
        Triangulo = [(self.x, self.y),( self.x-55,self.y+100),(self.x+50 , self.y+100)]
        pygame.draw.polygon(screen ,self.color, Triangulo )      
        
    def moverT(self, key):
        self.ex = 0
        self.ey = 0
        if key[pygame.K_DOWN]:
            self.ey += self.velocidad
        if key[pygame.K_UP]:
            self.ey -= self.velocidad
        if key[pygame.K_LEFT]:
            self.ex -= self.velocidad
        if key[pygame.K_RIGHT]:
            self.ex += self.velocidad
        
        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2)
        
        self.x += self.ex
        self.y += self.ey
    

        

