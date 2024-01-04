import pygame

#Inicilizar pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Titulo e icono
pygame.display.set_caption("Invacion espacial")
icono = pygame.image.load("astronauta.png")
pygame.display.set_icon(icono)


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
    pantalla.fill((110, 213, 239))
    pygame.display.update()
            
