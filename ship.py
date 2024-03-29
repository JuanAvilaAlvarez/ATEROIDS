import pygame
import math
from pygame.locals import *
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, contendedor):
        self.angulo = 0
        self.radio = 8
        self.puntos = 0
        self.vida = 100
        self.velocidad = [0, 0]
        self.bullets = []
        self.carga = True
        self.contendedor = contendedor
        self.image_base = pygame.image.load("images/ship.png")
        self.image = self.image_base
        self.rect = self.image.get_rect()
        self.rect.move_ip(contendedor[0]/2, contendedor[1]/2)
        self.impulso = pygame.mixer.Sound('sounds/impulso.wav')
        self.impulso.set_volume(0.05)
        self.disparo = pygame.mixer.Sound("sounds/disparo.wav")
        self.disparo.set_volume(0.05)

    def update(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_LEFT]:
            self.rotar(2)
        elif teclas[K_RIGHT]:
            self.rotar(-2)
        elif teclas[K_UP]:
            self.acelerar()

        self.velocidad[0] *= 0.99
        self.velocidad[1] *= 0.99

        self.rect = self.rect.move(self.velocidad)
        self.rect.x %= self.contendedor[0]
        self.rect.y %= self.contendedor[1]
        
    def disparar(self):
        self.disparo.play()
        vector = [0,0]
        vector[0] += math.cos
    
    def acelerar(self):
        self.velocidad[0] += math.cos(math.radians((self.angulo)%360))
        self.velocidad[1] -= math.cos(math.radians((self.angulo)%360))

    def rotar(self, angulo):
        self.angulo += angulo
        centro_x = self.rect.centerx
        centro_y = self.rect.centery
        self.image = pygame.transform.rotate(self.image_base, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.centerx = centro_x
        self.rect.centery = centro_y