
import pygame


pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()

window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
from load import *
# Set icon
#pygame.display.set_icon(pygame.image.load("Images\Icon\load.png").convert_alpha())
# Set title
pygame.display.set_caption("HatHome")

# Tick Init
clock = pygame.time.Clock()

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

    # [---[Update Display]---]
    #pygame.display.update()
