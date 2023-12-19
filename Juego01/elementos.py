import pygame
import math

class Avion:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        imagen1 = pygame.image.load("avion.png")
        imagen2 = pygame.image.load("avion2.png")
        self.avion1 = pygame.transform.scale(imagen1, (150, 150))
        self.avion2 = pygame.transform.scale(imagen2, (150, 150))
        self.avion = [self.avion1, self.avion2]
        self.contador = 0

    def moverDerecha(self):
        self.x += 1
        pantalla = pygame.display.get_surface()
        tamaño = pantalla.get_width()
        limite = tamaño - self.avion[0].get_width()
        self.x = min(self.x, limite)

    def moverIzquierda(self):
        self.x -= 1
        limite = 0
        self.x = max(self.x, limite)
    
    def dibujar(self):
        self.contador = (self.contador + 1) % 40
        pantalla = pygame.display.get_surface()
        seleccionada = self.contador // 20
        pantalla.blit(self.avion[seleccionada], (self.x, self.y))

class Fondo:
    def __init__(self) -> None:
        pantalla= pygame.display.get_surface()
        image = pygame.image.load("fondo.png")
        self.fondo=pygame.transform.scale(image,(pantalla.get_width(),image.get_height()))
        self.scroll = 0
        self.piezas =math.ceil(pantalla.get_height() / self.fondo.get_height()+ 1)

    def dibujar(self):
        self.scroll +=1
        pantalla=pygame.display.get_surface()
        if self.scroll>self.fondo.get_height():
            self.scroll = 0
        for i in range(0,self.piezas):
            pantalla.blit(self.fondo,(0,- self.fondo.get_height()+ i * self.fondo.get_height()+self.scroll))
    
