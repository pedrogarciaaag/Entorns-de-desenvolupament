import pygame
import elementos

pygame.init()
pantalla = pygame.display.set_mode((800,600))
reloj = pygame.time.Clock()
FPS=60
#imagen_avion =pygame.image.load("avion.png")
#avion = pygame.transform.scale(imagen_avion,(90,90))
#avion_rect = avion.get_rect()


salir = False

fondo = elementos.Fondo()
avion = elementos.Avion(300,450)

avion1= elementos.Avion(30,30)
avion2= elementos.Avion(300,300)

while not salir:
    reloj.tick(80)
    #gestionar eventos propios del juego
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            salir = True
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        avion.moverIzquierda()
    if teclas[pygame.K_RIGHT]:
        avion.moverDerecha()
    #if teclas[pygame.K_UP]:
       # posTop -= 1
    #if teclas[pygame.K_DOWN]:
       # posTop += 1

    #gestionar cambios(jugadores,teclas)
    #pantalla.fill((25,55,255))
    fondo.dibujar()
    #pantalla.blit(avion,(posIzda,posTop))
    avion.dibujar()
    
    #redibujar el juego
    pygame.display.flip()

pygame.quit()
