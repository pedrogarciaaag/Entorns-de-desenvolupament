import pygame
import elementos2
import random
from pygame.sprite import spritecollide

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
fondo = elementos2.Fondo()  
nave = elementos2.Nave(posicion)  

#crear grupo sprites
grupo_sprites = pygame.sprite.Group(fondo, nave) 

#crear grupo de balas
balas = pygame.sprite.Group()

#crear grupo de enemigos
enemigos = pygame.sprite.Group()

enemigo = elementos2.Enemigo((50,50))
grupo_sprites.add(enemigo)
enemigos.add(enemigo)

#varaible que alcance ultimo enemigo creado
ultimo_enemigo_creado = 0
frecuencia_enemigo_creado = 2000

#bucle principal
while running:
    #limitamos el bucle al framerate definido
    reloj.tick(FPS)

    #gestionar salida
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #creacion enemigos
    momento_actual = pygame.time.get_ticks()
    if(momento_actual > ultimo_enemigo_creado + frecuencia_enemigo_creado):
        cordX = random.randint(0,pantalla.get_width())
        cordY = 0
        enemigo = elementos2.Enemigo((cordX, cordY))  # Aquí está la corrección
        grupo_sprites.add(enemigo)
        enemigos.add(enemigo)
        ultimo_enemigo_creado = momento_actual

    #teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        bala = nave.disparar(grupo_sprites)
        if bala is not None:  # Aseguramos que bala no es None antes de añadirla a balas
            balas.add(bala)
    
    # Comprobamos si alguna bala ha colisionado con un enemigo
    for bala in balas:
        enemigos_golpeados = spritecollide(bala, enemigos, True)
        # Si la bala golpea a un enemigo, la eliminamos
        if enemigos_golpeados:
            bala.kill()
            
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
