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
        #running
        running = args[7]
        #vidas jugador
        vidas_jugador = args[9]

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

        grupo_sprites_enemigos = args[8]
        enemigos_colison= pygame.sprite.spritecollideany(self,grupo_sprites_enemigos,pygame.sprite.collide_mask)
        if enemigos_colison:
            enemigos_colison.kill()
            vidas_jugador.restarvidas_jugador()
            if vidas_jugador.getvidas_picolo() == 0 :
                running[0] = False
        
        grupo_sprites_rayo = args[10]
        rayo_colision = pygame.sprite.spritecollideany(self,grupo_sprites_rayo,pygame.sprite.collide_mask)
        if rayo_colision :
            rayo_colision.kill()
            vidas_jugador.restarvidas_jugador()
            if vidas_jugador.getvidas_picolo() == 0 :
                running[0] = False
        
class Kamehameha(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/kame.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.x +=5
        if self.rect.bottom < 0:
            self.kill()

        grupo_sprites_enemigos = args[8]
        enemigos_colison= pygame.sprite.spritecollideany(self,grupo_sprites_enemigos,pygame.sprite.collide_mask)
        if enemigos_colison:
            enemigos_colison.kill()
            self.kill()
        
class Picolo (pygame.sprite.Sprite):
    def __init__(self,posicion,velocidad) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/boss.png")
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        self.velocidad = velocidad
        self.ultimo_disparo = 0

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y -= self.velocidad
        if self.rect.y < 0:
            self.velocidad = -self.velocidad
        elif self.rect.y > pantalla.get_height() - self.image.get_height():
            self.velocidad = -self.velocidad

        #colision de picolo con la bala
        grupo_sprites_kame = args[2]
        vidas_picolo = args[6]
        running = args[7]
        colision = pygame.sprite.spritecollideany(self,grupo_sprites_kame,pygame.sprite.collide_mask)
        if colision:
            colision.kill()
            vidas_picolo.restarvida_picolo()
            if vidas_picolo.getvidas_picolo() <= 0 :
                running[0] = False

        grupo_sprites_todos = args[1]
        grupo_sprites_rayos = args[10]
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 1000:  
            self.disparar(grupo_sprites_todos, grupo_sprites_rayos) 
            self.ultimo_disparo = momento_actual
        
    #funcion para que jugador dispare rayo
    def disparar(self, grupo_sprites_todos, grupo_sprites_balas_picolo):
        bala = Rayo((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 2))
        grupo_sprites_balas_picolo.add(bala)
        grupo_sprites_todos.add(bala)

class Rayo(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/rayo.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.x -=5
        if self.rect.bottom < 0:
            self.kill()

class Enemigos(pygame.sprite.Sprite):
    def __init__(self,posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("Imagenes/picolo.png")
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.x -=1
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        self.rect.y = max(0, self.rect.y)
        self.rect.y = min(pantalla.get_height() - self.image.get_height(), self.rect.y)
        if (self.rect.x == 0):
            self.kill()


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

class Puntos ():
    def __init__(self) -> None:
        self.puntuacion = 0
        self.vidas_picolo = 1 
        self.vidas_jugador = 1

    def getvidas_picolo (self) :
        return self.vidas_picolo
    def restarvida_picolo(self):
        self.vidas_picolo-=1
    
    def getvidas_jugador(self):
        return self.vidas_jugador
    def restarvidas_jugador(self):
        self.vidas_jugador-=1

    def getpuntuacion (self):
        return self.puntuacion
    def sumarpuntuacion(self):
        self.puntuacion +=1