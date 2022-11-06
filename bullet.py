import pygame
from os import path

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("banana.png")
        self.rect = self.image.get_rect()
        
        # x and y are set at construction
        self.rect.bottom = y
        self.rect.centerx = x
        
        # go upward
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()