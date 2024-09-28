import pygame
import math as mt
from circulo201 import Circulo
from circulo202 import Circulo2

pygame.init()


icon = pygame.image.load("LLama.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Alo?")

run = True 
circulo1 = Circulo(250, 250, 50)
circulo2 = Circulo2(100, 100, 100)

def colision(C1, C2, radius1 , radius2):
        distance = mt.sqrt((C2.posicion()[0] - C1.posicion()[0] )**2 + (C2.posicion()[1] - C1.posicion()[1])**2)
        return distance <  (radius1 + radius2)

        

    
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    
    
    #guardando posiciones
    prev_posi1 = circulo1.posicion()
    prev_posi2 = circulo2.posicion()
    
    #Mover los circulos
    circulo1.move(key)
    circulo2.move(key)
    
    
    #colision
    if colision(circulo1, circulo2, circulo1.radius, circulo2.radius):
         circulo1.x,circulo1.y = prev_posi1
         circulo2.x,circulo2.y = prev_posi2
         circulo2.color = (200,200,100)
         circulo1.color = (200,200,100)     
    else:
         circulo1.color = (192,192,192)
         circulo2.color = (219,112,147)
    
    
    #Draw circulitos
    circulo1.draw(screen)
    circulo2.draw(screen)
    
    pygame.display.update()
pygame.quit()
