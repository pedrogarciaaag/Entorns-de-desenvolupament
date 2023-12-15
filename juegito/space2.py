import pygame
import elementos2
import random

#inicamos juego
pygame.init()

#creamos pantalla
tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

#creamos reloj
reloj = pygame.time.Clock()
FPS = 60

#booleano control
running = True

#crear nave
posicion = (100,450)
nave = elementos2.Nave(posicion)


#crear grupo sprites
grupo_sprites = pygame.sprite.Group(nave)

enemigo = elementos2.Enemigo((50,50))
grupo_sprites.add(enemigo)

#varaible que alcance ultimo enemigo creado
ultimo_enemigo_creado = 0

#bucle principal
while running:
    #limitamos el bucle al framerate definido
    reloj.tick(FPS)

    #gestionar salida
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    momento_actual = pygame.time.get_ticks()
    if(momento_actual > ultimo_enemigo_creado + 1000):
        cordX = random.randint(0,pantalla.get_width())
        cordY = 0
        grupo_sprites.add(elementos2.Enemigo((cordX, cordY)))  # Aquí está la corrección
        ultimo_enemigo_creado = momento_actual


    teclas = pygame.key.get_pressed()
    #pintar
    #el color de la pantalla
    pantalla.fill((0,0,0))
    #segundo los sprites
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)
    
    #redibujar la pantalla
    pygame.display.flip()

#finalizamos juego
pygame.quit()
