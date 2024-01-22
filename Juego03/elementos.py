import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        # Cargamos las imágenes
        self.imagenes_derecha = [pygame.image.load("goku_derecha.png")]
        self.imagenes_izquierda = [pygame.image.load("goku_izquierda.png")]
        self.imagenes = self.imagenes_derecha  
        self.indice_imagen = 0
        self.image = self.imagenes[self.indice_imagen]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.ultimo_disparo = 0
        self.vidas = 3
        self.puntuacion = 0

    #update
    def update(self, *args):
        teclas = args[0]
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
            self.imagenes = self.imagenes_izquierda  
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pygame.display.get_surface().get_width() - self.image.get_width(), self.rect.x)
            self.imagenes = self.imagenes_derecha 

        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)
        self.image = self.imagenes[self.indice_imagen]
        #Capturar grupo sprites enemigos 3
        grupo_sprites_enemigos = args[2]
        grupo_sprites_comida = args[3]
        #variable running
        running = args[4]
        vidas = args[5]
        puntuacion = args[6]

        #detectar colisiones
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos,pygame.sprite.collide_mask)
        if enemigo_colision:
            enemigo_colision.kill()
            self.vidas -=1
            vidas.restarvida()
            if vidas.getvidas() <= 0 :
                running[0] = False
        comida_colision = pygame.sprite.spritecollideany(self, grupo_sprites_comida,pygame.sprite.collide_mask)
        if comida_colision:
            comida_colision.kill()
            self.puntuacion += 1
            puntuacion.sumarpuntuacion()
            
            
class Puntos ():
    def __init__(self) -> None:
        self.puntuacion = 0
        self.vidas = 3 
        
    def getvidas (self) :
        return self.vidas
    def restarvida(self):
        self.vidas-=1

    def getpuntuacion (self):
        return self.puntuacion
    def sumarpuntuacion(self):
        self.puntuacion +=1
#creador de enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        imagen = pygame.image.load("aguja.png")
        imagen2 = pygame.transform.scale(imagen, (150, 150))
        self.image = pygame.transform.rotate(imagen2, 180)
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y += 1
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if (self.rect.y > pantalla.get_height()):
            self.kill()

class Comida(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        imagen_comida = pygame.image.load("comida.png")
        imagen2_comida = pygame.transform.scale(imagen_comida,(100,100))
        self.image = pygame.transform.rotate(imagen2_comida, 0)
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y += 1
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if (self.rect.y > pantalla.get_height()):
            self.kill()


class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # cargamos la imagen
        imagen = pygame.image.load("fondo1.png")
        #pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0, 0)