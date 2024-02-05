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
        self.ultimo_disparo = 0

    def disparar(self, grupo_sprites_todos, grupo_sprites_bala):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 500:
            bala = Kamehameha((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 2))
            grupo_sprites_bala.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_disparo = momento_actual

    def update(self, *args):
        #capturamos teclas
        teclas = args[0]
        #capturamos todos
        grupo_sprites_todos = args[1]
        #capturamos balas
        grupo_sprites_bala = args[2]
        grupo_sprites_esfera = args[3]

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
            self.disparar(grupo_sprites_todos, grupo_sprites_bala)

        if not any(teclas):
            self.image = self.image_normal

class Kamehameha(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("kame1.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.x +=5
        if self.rect.bottom < 0:
            self.kill()

class Esferas(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("esfera.png")
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
        self.tiempo_inicial = pygame.time.get_ticks()

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if (self.rect.y > pantalla.get_height()):
            self.kill()


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