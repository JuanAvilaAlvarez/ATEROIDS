import pygame
from pygame.locals import *
import sys
from ship import *

size = width, heigth = 800, 600

screen = pygame.display.set_mode(size)

def main():
    pygame.init()

    backgorund_image = pygame.image.load("images\space.png")
    backgorund_rect = backgorund_image.get_rect()

    pygame.display.set_caption("Asteroids")

    ship = Ship(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.update()        
        screen.blit(backgorund_image, backgorund_rect)
        screen.blit(ship.image, ship.rect)

        pygame.display.update()
        pygame.time.delay(10)
    
if __name__ == "__main__":
    main()