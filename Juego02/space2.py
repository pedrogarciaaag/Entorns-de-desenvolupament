import pygame
import elementos2
import random
import pygame_menu
#inicialicamos el juego
pygame.init()

#creamos la pantalla
tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

#creamos un reloj
reloj = pygame.time.Clock()
FPS =  60

#booleano de control
posicion = (100,450)
fondo = elementos2.Fondo()
nave = elementos2.Nave(posicion)
#crear un grupo de sprites
#grupo_sprites = pygame.sprite.Group(fondo)
#grupo_sprites.add(nave)

#grupo_sprites.add(elementos2.Nave((400,200)))
#grupo_sprites.add(elementos2.Nave((500,100)))
#grupo_sprites.add(elementos2.Nave((100,300)))

grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_bala = pygame.sprite.Group()

grupo_sprites_todos.add(fondo)
grupo_sprites_todos.add(nave)
#enemigo = elementos2.Enemigo((50,50))
#grupo_sprites.add(elementos2.Enemigo((70, 70)))

#crear u na variable que almacene la última creacion de enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 1500

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    running = [True]
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo
    global FPS
    global grupo_sprites_bala
    global grupo_sprites_todos
    global grupo_sprites_enemigos
    global reloj

    # bucle principal
    while running[0]:
        # Limitamos el bucle al framrate definido
        reloj.tick(FPS)
        # gestionar la salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        # creacion de enemigos
        momento_actual = pygame.time.get_ticks()
        if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
            cordX = random.randint(0, pantalla.get_width())
            cordY = 0
            enemigo = elementos2.Enemigo((cordX, cordY))
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
            ultimo_enemigo_creado = momento_actual

        # capturamos las teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
          running[0] = False

        # pintaremos:
        # pantalla.fill((255,255,255))
        grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala, grupo_sprites_enemigos, running)
        grupo_sprites_todos.draw(pantalla)

        # redibujar la pantala
        pygame.display.flip()
    pass

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)
#finalizamos el juego
pygame.quit()