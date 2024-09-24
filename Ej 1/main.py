import pygame 
from triangulo import Triangulo
from circulo import Circulo



pygame.init()

icon = pygame.image.load("LLama.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("PYgamer")

running = True 



personaje = Triangulo(400, 100)
personaje2 = Circu(200, 50)
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key = pygame.key.get_pressed()
 
    personaje.moverT(key)
    personaje2.moverC(key)
    
    
    personaje2.dibujarC(screen)
    personaje.dibujarT(screen)
    pygame.display.flip()

pygame.quit()