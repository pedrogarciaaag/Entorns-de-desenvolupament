import pygame
import elementos1
import pygame_menu

pygame.init()

#Pantalla y su tamaño
pantalla = pygame.display.set_mode((1366,768))

personaje = elementos1.Jugador()

#Cargamos el fondo
fondo = pygame.image.load("..\\Imagenes\\fondo1.png")

reloj = pygame.time.Clock()

def start_the_game ():
    running = [True]
    global reloj

    while running [0]:
        reloj.tick(90)
        personaje.update()
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False]

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
          running[0] = False

        # fill the screen with a color to wipe away anything from last frame
        pantalla.blit(fondo,(0,0))
        pantalla.blit(personaje.image,personaje.rect)

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