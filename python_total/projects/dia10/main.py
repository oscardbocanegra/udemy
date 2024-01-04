import pygame

#Inicilizar pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Titulo e icono
pygame.display.set_caption("Invacion espacial")
icono = pygame.image.load("astronauta.png")
pygame.display.set_icon(icono)

#Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 536

def jugador():
    pantalla.blit(img_jugador, (jugador_x, jugador_y))


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #RGB
    pantalla.fill((110, 213, 239))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    
    jugador()
    
    pygame.display.update()
            
