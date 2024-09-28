import pygame


class Circulo():
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.color = (192,192,192)
        self.velocidad = 0.5

    def dibujarC(self, screen):
        circulo = (self.x ,self.y)
        pygame.draw.circle(screen , self.color , circulo, 20)

    def moverC(self, key):
        if key[pygame.K_s]:
            self.y += self.velocidad
        if key[pygame.K_w]:
            self.y -= self.velocidad
        if key[pygame.K_a]:
            self.x -= self.velocidad
        if key[pygame.K_d]:
            self.x += self.velocidad
           
 
