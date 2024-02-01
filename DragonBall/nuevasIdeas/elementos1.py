import pygame
from pygame.sprite import Group

class Jugador (pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.image = pygame.image.load("kid.png")
        self.imagenes = self.image
        self.rect = self.image.get_rect()

    def update(self, *args) -> None:
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.image = pygame.image.load("kid1.png")
            self.rect.y -= 2
            self.rect.y = max(0, self.rect.y)
        elif teclas[pygame.K_DOWN]:
            self.image = pygame.image.load("kid2.png")
            self.rect.y += 2
            pantalla = pygame.display.get_surface()
            self.rect.y = min(pantalla.get_height() - self.image.get_height(), self.rect.y)

        if teclas[pygame.K_LEFT]:
            self.image = pygame.image.load("kid4.png")
            self.rect.x -= 2
            self.rect.x = max(0,self.rect.x)
        elif teclas[pygame.K_RIGHT]:
            self.image = pygame.image.load("kid3.png")
            self.rect.x += 2
            pantalla = pygame.display.get_surface()
            self.rect.x = min(pantalla.get_width ()- self.image.get_width(),self.rect.x)
        
        if teclas[pygame.K_SPACE]:
            self.image = pygame.image.load("kidkame.png")

        if not any(teclas):
            self.image = pygame.image.load("kid.png")

# class Kamehameha (pygame.sprite.Sprite):
#     def __init__(self) -> None:
#         self.image = pygame.image.load("kame.png")
#         self.rect = self.image.get_rect()

#     def update(self) -> None:
#         teclas = pygame.key.get_pressed()
#         if teclas[pygame.K_SPACE]:
#                 self.rect.x = (self.rect.x + 5)
#                 self.rect.y = (self.rect.y + 0)

