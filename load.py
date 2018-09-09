'''
load the images etc...
'''
from tools import *

spriteplayer = tools.separate("Assets\Image\SpritePlayer.png", 26, 30)
icon = pygame.transform.scale(pygame.image.load("Assets\Image\Icon.png").convert_alpha(), (32, 32))     #convert alpha use the transparence
