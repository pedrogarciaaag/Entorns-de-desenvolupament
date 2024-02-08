from typing import Any
import pygame

class Jugador (pygame.sprite.Sprite):
    def __init__(self,posicion):
        super().__init__()
        #creacion de array de las imagenes
        self.imagenes = [
            pygame.image.load("Imagenes/kid.png"),  # normal
            pygame.image.load("Imagenes/kid1.png"),  # arriba
            pygame.image.load("Imagenes/kid2.png"),  # abajo
            pygame.image.load("Imagenes/kid3.png"),  # derecha
            pygame.image.load("Imagenes/kid4.png"),  # izquierda
            pygame.image.load("Imagenes/kidkame.png")  # kame
        ]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.ultimo_disparo = 0
        self.puntuacion = 0

    #funcion para que jugador dispare kame
    def disparar(self, grupo_sprites_todos, grupo_sprites_kame):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 500:
            bala = Kamehameha((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 2))
            grupo_sprites_kame.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_disparo = momento_actual

    def update(self, *args):
        #capturamos teclas
        teclas = args[0]
        #capturamos todos
        grupo_sprites_todos = args[1]
        #capturamos kames
        grupo_sprites_kame = args[2]
        #capturamos esferas
        grupo_sprites_esfera = args[3]
        #capturamos puntuacion esferas
        puntuacion = args[5]

        if teclas[pygame.K_UP]:
            self.image = self.imagenes[1]
            self.rect.y -= 2
            self.rect.y = max(0, self.rect.y)
        elif teclas[pygame.K_DOWN]:
            self.image = self.imagenes[2]
            self.rect.y += 2
            pantalla = pygame.display.get_surface()
            self.rect.y = min(pantalla.get_height() - self.image.get_height(), self.rect.y)

        if teclas[pygame.K_LEFT]:
            self.image = self.imagenes[4]
            self.rect.x -= 2
            self.rect.x = max(0,self.rect.x)
        elif teclas[pygame.K_RIGHT]:
            self.image = self.imagenes[3]
            self.rect.x += 2
            pantalla = pygame.display.get_surface()
            self.rect.x = min(pantalla.get_width ()- self.image.get_width(),self.rect.x)
        
        if teclas[pygame.K_SPACE]:
            self.image = self.imagenes[5]
            self.disparar(grupo_sprites_todos, grupo_sprites_kame)

        if not any(teclas):
            self.image = self.imagenes[0]

        #colisiones esferas
        esfera_colison  = pygame.sprite.spritecollideany(self,grupo_sprites_esfera,pygame.sprite.collide_mask)
        if esfera_colison : 
            esfera_colison.kill()
            puntuacion.sumarpuntuacion()

class Puntos ():
    def __init__(self) -> None:
        self.puntuacion = 0

    def getpuntuacion (self):
        return self.puntuacion
    def sumarpuntuacion(self):
        self.puntuacion +=1

class Kamehameha(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/kame1.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.x +=5
        if self.rect.bottom < 0:
            self.kill()
        
        #colison con picolo
        grupo_sprites_picolo =args[4]
        picolo_colision = pygame.sprite.spritecollideany(self,grupo_sprites_picolo,pygame.sprite.collide_mask)
        if picolo_colision:
            self.kill()
            picolo_colision.kill()

class Picolo (pygame.sprite.Sprite):
    def __init__(self,posicion,velocidad) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/picolo.png")
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        self.velocidad = velocidad

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y -= self.velocidad
        if self.rect.y < 0:
            self.velocidad = -self.velocidad
        elif self.rect.y > pantalla.get_height() - self.image.get_height():
            self.velocidad = -self.velocidad


class Esferas(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/esfera.png")
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
        self.tiempo_inicial = pygame.time.get_ticks()

    #update para que max y min de pantalla y cuando salga se autokill
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
        imagen = pygame.image.load("Imagenes/fondo1.png")
        #pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0, 0)