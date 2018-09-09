
import pygame
from entity import *

pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()

window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

from load import *

# Set icon
pygame.display.set_icon(icon)

# Set title
pygame.display.set_caption("HatHome")

# Set Music
pygame.mixer.music.load("Assets\Music\music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(4)

# Tick Init
clock = pygame.time.Clock()

# Create player
player = Player(50, 50, 5, spriteplayer, 10, 1)

# Main loop
run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Exit Control
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.QUIT]:
        run = False

    # Control
    if keys[pygame.K_w]:
        player.up()
    if keys[pygame.K_s]:
        player.down()
    if keys[pygame.K_a]:
        player.left()
    if keys[pygame.K_d]:
        player.right()

    pygame.draw.rect(window,(50,50,50),(0,0,1600,900))
    player.display(window)

    # [---[Update Display]---]
    pygame.display.update()
