import pygame

class Triangulo():
    def __init__(self, x ,y):
        self.x = x
        self.y = y 
        self.color = "red"
        self.velocidad = 0.5
        
    def dibujarT(self,screen):
        Triangulo = [(self.x, self.y),( self.x-55,self.y+100),(self.x+50 , self.y+100)]
        pygame.draw.polygon(screen ,self.color, Triangulo )      
        
    def moverT(self,key):
        if key[pygame.K_s]:
            self.y += self.velocidad
        if key[pygame.K_w]:
            self.y -= self.velocidad
        if key[pygame.K_a]:
            self.x -= self.velocidad
        if key[pygame.K_d]:
            self.x += self.velocidad



        

