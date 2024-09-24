import pygame


class Circulo():
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.color = (192,192,192)
        self.velocidad = 0.2

    def dibujarC(self, screen):
        circulo = (self.x ,self.y)
        pygame.draw.circle(screen , self.color , circulo, 20)

    def moverC(self, key):
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
            self.ex /= 1.414
            self.ey /= 1.414
        
        self.x += self.ex
        self.y += self.ey
    
    def colision(self):
        pass

 
