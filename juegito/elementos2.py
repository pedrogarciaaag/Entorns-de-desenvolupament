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
        self.contador_imagen = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

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
        self.contador_imagen = (self.contador_imagen+1)%40
        self.indice_image = self.contador_imagen // 20
        old_center = self.rect.center
        self.image = self.array_imagenes_rotadas_y_escaladas[self.indice_image]
        self.rect = self.image.get_rect()
        self.rect.center = old_center

class Enemigo (pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        imagen = pygame.image.load("enemigo1.png")
        self.image = pygame.transform.scale(imagen, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y +=1
