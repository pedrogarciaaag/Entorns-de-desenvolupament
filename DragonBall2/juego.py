import pygame
import elementos1
import pygame_menu
import random

#inicializamos el juego
pygame.init()

#Creamos pantalla y su tamaño
pantalla = pygame.display.set_mode((1366,768))

#creamos la frecuencia de creacion de esferas
ultimo_esferas_creado = 0
frecuencia_creacion_esferas = 10000

#creacion la creacion de enemigos
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 2000

#velocidad para picolo
velocidad = 3
#creamos un reloj 
reloj = pygame.time.Clock()

#Fuente letras 
font= pygame.font.Font(pygame_menu.font.FONT_8BIT,20)

def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    global velocidad
    frecuencia_creacion_enemigo = difficulty

def start_the_game ():
    running = [True]
    global reloj
    global ultimo_esferas_creado
    global frecuencia_creacion_esferas
    global ultimo_enemigo_creado
    global frecuencia_creacion_enemigo

    #Cargamos personaje y su posicion
    posicion=(100 ,350)
    personaje = elementos1.Jugador(posicion)

    #Cargamos el fondo
    fondo = elementos1.Fondo()

    #cargamos picolo, su posicon y su velocidad inicial
    picolo = elementos1.Picolo((1200,500),velocidad)

    #creamos grupo de sprites de todo
    grupo_sprites_todos = pygame.sprite.Group()
    #creamos grupo de sprites del kame cada vez que dispare
    grupo_sprites_kame = pygame.sprite.Group()
    #creamos el grupo de sprites de las esferas que se iran creando
    grupo_sprites_esfera = pygame.sprite.Group()
    #creamos grupo de sprites de picolo
    grupo_sprites_picolo = pygame.sprite.Group()

    grupo_sprites_rayos = pygame.sprite.Group()
    #creamos grupo sprites enemigos
    grupo_sprites_enemigos = pygame.sprite.Group()

    grupo_sprites_todos.add(fondo)
    grupo_sprites_todos.add(personaje)
    grupo_sprites_todos.add(picolo)

    grupo_sprites_picolo.add(picolo)

    pausado = False

    puntuacion_esferas = elementos1.Puntos()
    vidas_picolo = elementos1.Puntos()
    vidas_jugador = elementos1.Puntos()

    #bucle princiapl
    while running [0]:
        reloj.tick(90)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        #capturamos teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
          running[0] = False
        if teclas[pygame.K_b]:
            pausado = not pausado

        if not pausado:
            #update funcion principal
            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_kame,grupo_sprites_esfera,grupo_sprites_picolo,puntuacion_esferas,vidas_picolo,running,grupo_sprites_enemigos,vidas_jugador,grupo_sprites_rayos)
            #obtenemos los ticks del juego para la creacion de esferas
            momento_actual = pygame.time.get_ticks()
            
            # creacion de esferas
            if momento_actual > ultimo_esferas_creado + frecuencia_creacion_esferas:
                    #cordenadas X de aparcicion esferas(no sobrepasan a picolo)
                    cordX = random.randint(0,1200)
                    cordY = random.randint(0,pantalla.get_height())
                    esfera = elementos1.Esferas((cordX, cordY))
                    grupo_sprites_todos.add(esfera)
                    grupo_sprites_esfera.add(esfera)
                    ultimo_esferas_creado = momento_actual

            #creacion enemigos
            if momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo:
                cordX = 1366
                cordY = random.randint(0,pantalla.get_height())
                enemigo = elementos1.Enemigos((cordX, cordY))
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                ultimo_enemigo_creado = momento_actual

        #pintamos todo los sprites en la pantalla
        grupo_sprites_todos.draw(pantalla)
        if pausado:
            texto = font.render("PAUSADO",True,"White")
            pantalla.blit(texto,(pantalla.get_width()//2 - texto.get_width()//2, pantalla.get_height()//2 - texto.get_height()//2))
            valor_puntuacion = font.render("Esferas del dragon " +str(puntuacion_esferas.getpuntuacion()),True,"Orange")
            pantalla.blit(valor_puntuacion, (250, 70))

        # if not pausado : 
        #      valor_puntuacion = font.render("Esferas del dragon " +str(puntuacion_esferas.getpuntuacion()),True,"Orange")
        #      pantalla.blit(valor_puntuacion, (250, 70))

        # #icono de goku arriba izquierda
        # goku_icono = pygame.image.load("Imagenes/goku_icono.png")
        # pantalla.blit(goku_icono, (0, 0))
        # #icono de picolo arriba derecha
        # picolo_icono  = pygame.image.load("Imagenes/picolo_icono.png")
        # pantalla.blit(picolo_icono,(1280,0))

        #si las vidas de picolo llegan a 0 el jugador gana 
        if vidas_picolo.getvidas_picolo() == 0:
            hasganado = pygame.image.load("Imagenes/hasganado.png")
            pantalla.blit(hasganado,(pantalla.get_width()//2 - hasganado.get_width()//2, pantalla.get_height()//2 - hasganado.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(3000)

        if vidas_jugador.getvidas_jugador() == 0:
            hasperdido = pygame.image.load("Imagenes/hasperdido.png")
            pantalla.blit(hasperdido,(pantalla.get_width()//2 - hasperdido.get_width()//2, pantalla.get_height()//2 - hasperdido.get_height()//2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = [False]

        pygame.display.flip()

#Imagen fondo menu
myimage = pygame_menu.baseimage.BaseImage(
    image_path="Imagenes/menu.png",
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
#creacion del menu
menu = pygame_menu.Menu('DragonBall Game', 1366,768, theme=tema)

menu.add.selector('Dificultad ', [('Facil', float('inf') ),('Dificil', 3000)], onchange=set_difficulty)
menu.add.button('Jugar', start_the_game)
menu.add.button('Salir', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

pygame.quit()