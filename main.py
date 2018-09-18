from tools import *
import pygame
from entity import *
from tools import *
from player import *


pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()

window = pygame.display.set_mode((tools.w0, tools.h0), pygame.FULLSCREEN)

from text_box import *
from load import *

text = Box()    #Initialise la boite de texte

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
    #UP
    if keys[pygame.K_w]:
        if keys[pygame.K_a]:
            player.upleft()
        elif keys[pygame.K_d]:
            player.upright()
        else:
            player.up()

    #DOWN
    elif keys[pygame.K_s]:
        if keys[pygame.K_a]:
            player.downleft()
        elif keys[pygame.K_d]:
            player.downright()
        else:
            player.down()

    #LEFT
    elif keys[pygame.K_a]:
        player.left()

    #RIGHT
    elif keys[pygame.K_d]:
        player.right()


    window.blit(background, (0,0))

    if keys[pygame.K_t]:        #juste pour le test si la touche t est pressé cela fait apparaitre un texte
        text.display(window)

    player.display(window)

    # [---[Update Display]---]
    pygame.display.update()
