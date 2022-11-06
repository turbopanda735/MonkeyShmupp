import pygame
import random
from os import path

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 800


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load("panther.png")
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        # where they spawn
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

        # entity speed
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # moving pixels based on randomized speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # spin sprites
        self.rotate()

        # if sprite goes off the map
        # return it to spawn point
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
			# do rotation here