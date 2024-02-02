import pygame

class Jugador (pygame.sprite.Sprite):
    def __init__(self,posicion):
        super().__init__()
        self.image = pygame.image.load("kid.png")
        self.image_normal = pygame.image.load("kid.png")
        self.image_arriba = pygame.image.load("kid1.png")
        self.image_abajo = pygame.image.load("kid2.png")
        self.image_derecha = pygame.image.load("kid3.png")
        self.image_izquierda = pygame.image.load("kid4.png")
        self.image_kame = pygame.image.load("kidkame.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

    def update(self, *args):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.image = self.image_arriba
            self.rect.y -= 2
            self.rect.y = max(0, self.rect.y)
        elif teclas[pygame.K_DOWN]:
            self.image = self.image_abajo
            self.rect.y += 2
            pantalla = pygame.display.get_surface()
            self.rect.y = min(pantalla.get_height() - self.image.get_height(), self.rect.y)

        if teclas[pygame.K_LEFT]:
            self.image = self.image_izquierda
            self.rect.x -= 2
            self.rect.x = max(0,self.rect.x)
        elif teclas[pygame.K_RIGHT]:
            self.image = self.image_derecha
            self.rect.x += 2
            pantalla = pygame.display.get_surface()
            self.rect.x = min(pantalla.get_width ()- self.image.get_width(),self.rect.x)
        
        if teclas[pygame.K_SPACE]:
            self.image = self.image_kame

        if not any(teclas):
            self.image = self.image_normal

# class Kamehameha (pygame.sprite.Sprite):
#     def __init__(self) -> None:
#         self.image = pygame.image.load("kame.png")
#         self.rect = self.image.get_rect()

#     def update(self) -> None:
#         teclas = pygame.key.get_pressed()
#         if teclas[pygame.K_SPACE]:
#                 self.rect.x = (self.rect.x + 5)
#                 self.rect.y = (self.rect.y + 0)

class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # cargamos la imagen
        imagen = pygame.image.load("..\\Imagenes\\fondo1.png")
        #pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0, 0)