import pygame

class Cuadrado():
    def __init__(self, x ,y):
        self.x = x
        self.y = y 
        self.color = "blue"
        self.velocidad = 0.5
        
    def dibujar(self,screen):
        cuadrado = [(self.x, self.y)]
        pygame.draw.rect(screen ,self.color, cuadrado)      
        
    def mover(self,key):
        if key[pygame.K_k]:
            self.y += self.velocidad
        if key[pygame.K_i]:
            self.y -= self.velocidad
        if key[pygame.K_j]:
            self.x -= self.velocidad
        if key[pygame.K_l]:
            self.x += self.velocidad



        

