import pygame
from circulo2 import Circulo
pygame.init()


icon = pygame.image.load("LLama.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Alo?")

run = True 
circulo1 = Circulo(250, 250)
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    circulo1.dibujarC(screen)
    circulo1.moverC(key)
    pygame.display.update()
pygame.quit()
