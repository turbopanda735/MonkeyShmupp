# pygame template
import pygame
import random
from player import Player
from mob import Mob
from bullet import Bullet
from os import path


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# window settings
WIDTH = 800
HEIGHT = 800
FPS = 60

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Shmup")
clock = pygame.time.Clock()


img_dir = path.join(path.dirname(__file__), "img")

# load all game graphics
background = pygame.image.load("jungle.jpg").convert()
background_rect = background.get_rect()

 
# player object
player = Player()

# sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# mobs
for i in range(0, 8):
    m = Mob()
    all_sprites.add(m )
    mobs.add(m)

score = 0
    
# game loop
run = True
while run:
    # keep loop running at correct speed
    clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            run = False;
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets)

    # update
    all_sprites.update()

    # does bullet hit mob?
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        score += 1

    # does mob hit player?
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        run = False

    # draw/render
    screen.fill(BLACK)
    
    # add background before sprites!
    screen.blit(background, background_rect)

    # add score before sprites
    font = pygame.font.SysFont('comicsans', 100)
    text = font.render(str(score), False, WHITE)
    screen.blit(text, (100, 100))
    
    #add sprites last!
    all_sprites.draw(screen)


    # always do this after drawing, flip the display
    pygame.display.flip()

pygame.quit()