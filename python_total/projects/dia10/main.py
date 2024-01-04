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
jugador_x_cambio = 0

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #RGB
    pantalla.fill((110, 213, 239))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            elif evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
                
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                
    jugador_x += jugador_x_cambio
    jugador(jugador_x, jugador_y)
    
    pygame.display.update()
            
