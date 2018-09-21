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
home = Player(50, 50, spriteplayer[0], 100, 5, spriteplayer)

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

    #Controlkeys
    window.blit(background, (0,0))
    home.be(window, keys, mouse, click)

    #Update Display
    pygame.display.update()
