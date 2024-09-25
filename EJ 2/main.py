import pygame
from circulo201 import Circulo
from circulo202 import Circulo2
pygame.init()


icon = pygame.image.load("LLama.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Alo?")

run = True 
circulo1 = Circulo(250, 250, 50)
circulo2 = Circulo2(200, 200, 50)
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    
    #Circulo 1 methodos 
    circulo1.draw(screen)
    circulo1.move(key)
    

    #Circulo 2 methodos
    circulo2.draw(screen)
    circulo2.move(key)

    #colision
    circulo1.colision(circulo2)
    circulo2.colision(circulo1)
    
    if circulo1.collision and circulo2.collision:
        circulo2.color = (178,34,34)
        circulo1.color = (178,34,34)
    else:
        circulo1.color = (192,192,192)
        circulo2.color = (219,112,147)
    
    pygame.display.update()
pygame.quit()
