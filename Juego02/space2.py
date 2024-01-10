import pygame
import elementos2
import random
import pygame_menu

pygame.init()

tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

reloj = pygame.time.Clock()
FPS =  60

font= pygame.font.Font(None,30)

posicion = (350, 500)  # Cambiado para centrar la nave
fondo = elementos2.Fondo()
nave = elementos2.Nave(posicion)

grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_bala = pygame.sprite.Group()

grupo_sprites_todos.add(fondo)
grupo_sprites_todos.add(nave)

ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 1500

def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    frecuencia_creacion_enemigo = difficulty

def start_the_game():
    running = [True]
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo
    global FPS
    global reloj

    posicion = (350, 500)
    nave = elementos2.Nave(posicion)
    
    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_bala = pygame.sprite.Group()

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
            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala, grupo_sprites_enemigos, running)
            momento_actual = pygame.time.get_ticks()
            if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                cordX = random.randint(0, pantalla.get_width())
                cordY = 0
                enemigo = elementos2.Enemigo((cordX, cordY))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual
        
        grupo_sprites_todos.draw(pantalla)
        if pausado:
            texto = font.render("PAUSADO",True,"White")
            pantalla.blit(texto,(pantalla.get_width()//2 - texto.get_width()//2, pantalla.get_height()//2 - texto.get_height()//2))  # Cambiado para centrar el texto "PAUSADO"
        pygame.display.flip()

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 200), ('Easy', 2000)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

pygame.quit()
