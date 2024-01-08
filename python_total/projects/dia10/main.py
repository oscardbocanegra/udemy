import pygame
import random
import math
from pygame import mixer

#Inicilizar pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Titulo e icono
pygame.display.set_caption("Invacion espacial")
icono = pygame.image.load("astronauta.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('cielo.jpg')

#agregar musica 
mixer.music.load('musica_fondo.mp3')
mixer.music.play(-1)


#Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("astronave.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)

#variables de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# funcion mostrar puntaje 
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

#funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))
    
#funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))
    
#funcion bala 
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#funcion detectar coliciones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        False

#Loop del juego
se_ejecuta = True
while se_ejecuta:
    
    #imagen de fondo
    pantalla.blit(fondo, (0,0))
    
    #iterar evento
    for evento in pygame.event.get():
        
        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
            
        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            elif evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            elif evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(jugador_x, bala_y)
                
        #Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                
                
    # Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio
    
    #Mantener dentro de bordes del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    # Modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
    
        #Mantener dentro de bordes del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
            
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
            
        #colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colicion = mixer.Sound('golpe.mp3')
            sonido_colicion.play()
            bala_y = 500
            bala_visible = False 
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    #movimiento bala
    if bala_y <= -64:
        bala_y =  500
        bala_visible = False
    
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio   
        
    
    jugador(jugador_x, jugador_y)
    
    mostrar_puntaje(texto_x, texto_y)
    
    #Actualizar
    pygame.display.update()
            
