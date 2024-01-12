import pygame
import elementos
import random
import pygame_menu

pygame.init()

tamaño = (1366,768)
pantalla = pygame.display.set_mode(tamaño)

reloj = pygame.time.Clock()
FPS =  60

font= pygame.font.Font(None,30)

posicion = (683, 424)  
fondo = elementos.Fondo()
nave = elementos.Nave(posicion)

grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_comida = pygame.sprite.Group()

grupo_sprites_todos.add(fondo)
grupo_sprites_todos.add(nave)

ultimo_enemigo_creado = 1500
frecuencia_creacion_enemigo = 3000

ultimo_comida_creado = 0
frecuencia_creacion_comida = 3000

def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    frecuencia_creacion_enemigo = difficulty

def start_the_game():
    running = [True]
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo
    global ultimo_comida_creado
    global frecuencia_creacion_comida
    global FPS
    global reloj

    posicion = (683, 424)
    nave = elementos.Nave(posicion)
    
    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_comida = pygame.sprite.Group()

    grupo_sprites_todos.add(fondo)
    grupo_sprites_todos.add(nave)

    pausado = False

    while running[0]:
        reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
          running[0] = False
        if teclas[pygame.K_p]:
            pausado = not pausado

        if not pausado:
            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_enemigos,grupo_sprites_comida, running)
            momento_actual = pygame.time.get_ticks()
            # enemigos
            if momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo:
                cordX = random.randint(0, pantalla.get_width())
                cordY = 0
                enemigo = elementos.Enemigo((cordX, cordY))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual
            #comida
            if momento_actual > ultimo_comida_creado + frecuencia_creacion_comida:
                cordX = random.randint(0, pantalla.get_width())
                cordY = 0
                comida = elementos.Comida((cordX,cordY))
                grupo_sprites_todos.add(comida)
                grupo_sprites_comida.add(comida)
                ultimo_comida_creado = momento_actual

        grupo_sprites_todos.draw(pantalla)
        if pausado:
            texto = font.render("PAUSADO",True,"Red")
            pantalla.blit(texto,(pantalla.get_width()//2 - texto.get_width()//2, pantalla.get_height()//2 - texto.get_height()//2))  # Cambiado para centrar el texto "PAUSADO"
        pygame.display.flip()

menu = pygame_menu.Menu('DragonBall game', 400, 300, theme=pygame_menu.themes.THEME_ORANGE)

menu.add.selector('Dificultad :', [('Difícil', 1000), ('Facil', 3000)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

pygame.quit()
