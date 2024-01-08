from typing import Any
import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self,posicion) -> None:
        super().__init__()
        #creamos imagen
        self.array_imagenes = [pygame.image.load("avioncito.png"), pygame.image.load("avioncito2.png")]
        self.array_imagenes_rotadas = [pygame.transform.rotate(self.array_imagenes[0], 90), pygame.transform.rotate(self.array_imagenes[1], 90)]
        self.array_imagenes_rotadas_y_escaladas = [pygame.transform.scale(img, (150, 150)) for img in self.array_imagenes_rotadas]
        
        self.indice_image = 0
        self.image = self.array_imagenes_rotadas_y_escaladas[self.indice_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

        # Inicializamos contador_imagen aquí
        self.contador_imagen = 0

        # Inicializamos contador_disparo aquí
        self.contador_disparo = 0

    #update
    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        pantalla = pygame.display.get_surface()
        if teclas[pygame.K_LEFT]:
            self.rect.x -=2
            self.rect.x = max(0,self.rect.x)
        if teclas[pygame.K_RIGHT]:
            self.rect.x +=2
            self.rect.x = min(pantalla.get_width()-self.image.get_width(), self.rect.x)

        #gestionamos animacion
        self.contador_imagen = (self.contador_imagen+1) % 40
        self.indice_image = self.contador_imagen // 20
        old_center = self.rect.center
        self.image = self.array_imagenes_rotadas_y_escaladas[self.indice_image]
        self.rect = self.image.get_rect()
        self.rect.center = old_center

        # Incrementamos contador_disparo
        self.contador_disparo += 1

    def disparar(self,grupo_sprites):
        # Solo disparamos si contador_disparo es mayor que un cierto valor
        if self.contador_disparo > 25:
            bala = Bala((self.rect.x + self.image.get_width() / 2,self.rect.y)) 
            grupo_sprites.add(bala)
            # Reiniciamos contador_disparo a 0 después de disparar
            self.contador_disparo = 0
            return bala  # Devolvemos la bala que acabamos de crear


class Enemigo (pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        imagen = pygame.image.load("enemigo1.png")
        self.image = pygame.transform.scale(imagen, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y +=1
        pantalla = pygame.display.get_surface()
        if(self.rect.y > pantalla.get_height()):
            self.kill()

class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        imagen = pygame.image.load("univer.png")  # Asegúrate de que el nombre del archivo y la extensión sean correctos
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), pantalla.get_height()))  # Asegúrate de escalar la imagen al tamaño de la pantalla
        self.rect = self.image.get_rect()

class Bala (pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.Surface((5,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y -= 5
        # Añadimos una comprobación para eliminar la bala si sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()