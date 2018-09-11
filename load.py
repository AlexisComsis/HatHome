'''
load the images etc...
'''
from tools import *

spriteplayer = tools.separate("Assets\Image\SpritePlayer.png", 78)
icon = pygame.transform.scale(pygame.image.load("Assets\Image\Icon.png").convert_alpha(), (32, 32))     #convert alpha use the transparence
background = pygame.image.load("Assets\Image\Room.png").convert_alpha()
background = pygame.transform.scale(background.convert_alpha(), (1920, 1080))
