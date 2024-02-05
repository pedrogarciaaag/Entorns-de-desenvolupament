import pygame
import elementos1
import pygame_menu
import random

pygame.init()

#Creamos pantalla y su tamaño
pantalla = pygame.display.set_mode((1366,768))

#Cargamos personaje
posicion=(100 ,350)
personaje = elementos1.Jugador(posicion)

#Cargamos el fondo
fondo = elementos1.Fondo()

#creamos grupo de sprites de todo
grupo_sprites_todos = pygame.sprite.Group()
#creamos grupo de sprites de la bala
grupo_sprites_bala = pygame.sprite.Group()
#
grupo_sprites_esfera = pygame.sprite.Group()
#añadimos al grupo de sprites el personaje y fondo
grupo_sprites_todos.add(fondo)
grupo_sprites_todos.add(personaje)

ultimo_esferas_creado = 2000
frecuencia_creacion_esferas = 3000

#creamos un reloj 
reloj = pygame.time.Clock()

def start_the_game ():
    running = [True]
    global reloj
    global ultimo_esferas_creado
    global frecuencia_creacion_esferas

    posicion=(100 ,350)
    personaje = elementos1.Jugador(posicion)

    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_bala = pygame.sprite.Group()
    grupo_sprites_esfera = pygame.sprite.Group()
    grupo_sprites_todos.add(fondo)
    grupo_sprites_todos.add(personaje)

    while running [0]:
        reloj.tick(90)
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
          running[0] = False

        grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_bala,grupo_sprites_esfera)
        momento_actual = pygame.time.get_ticks()
            # esferas
        if momento_actual > ultimo_esferas_creado + frecuencia_creacion_esferas:
                cordX = random.randint(0, pantalla.get_width())
                cordY = random.randint(pantalla.get_height,0)
                esfera = elementos1.Esferas((cordX, cordY))
                grupo_sprites_todos.add(esfera)
                grupo_sprites_esfera.add(esfera)
                ultimo_enemigo_creado = momento_actual

        grupo_sprites_todos.draw(pantalla)

        valor_vidas = pygame.image.load("prueba.png")
        pantalla.blit(valor_vidas, (0, 0))

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()


#Fuente letras menu
font= pygame.font.Font(pygame_menu.font.FONT_8BIT,20)

#Imagen fondo menu
myimage = pygame_menu.baseimage.BaseImage(
    image_path="..\\Imagenes\\menu.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

# Tema del menu
tema = pygame_menu.themes.Theme(
    background_color=myimage, 
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
    title_background_color=(255, 128, 0),
    title_font_shadow=True,
    title_font=pygame_menu.font.FONT_8BIT,
    title_font_size=50,
    widget_padding=35,
    widget_font=pygame_menu.font.FONT_8BIT,
    widget_font_size=35,
    widget_font_color = (255, 255, 255),
)

menu = pygame_menu.Menu('DragonBall Game', 1366,768, theme=tema)

menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

pygame.quit()