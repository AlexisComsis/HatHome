from tools import *
import pygame
#HEEY


pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()

window = pygame.display.set_mode((tools.w0, tools.h0), pygame.FULLSCREEN)

from entity import *
from gameobject import *
from load import *
from player import *

# Set icon
pygame.display.set_icon(icon)

# Set title
pygame.display.set_caption("HatHome")

# Set Music
pygame.mixer.music.load("HatHome\Assets\Music\music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(4)

# Tick Init
clock = pygame.time.Clock()

# Create player

p = []
p.append(background)
x1 = tools.convert_coord(800,450)[0] -34
y2 = tools.convert_coord(800,450)[1] -78
home = Player(10, 5, spriteplayer[0], spriteplayer, x1, y2)
background = Entity(background, p, 0, 0)
bugman = Entity(spritebuggman[0], spritebuggman, 400, 350)
