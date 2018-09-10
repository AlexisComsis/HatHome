'''
load the images etc...
'''
from tools import *

spriteplayer = tools.separate("Assets\Image\SaveSpritePlayer.png", 26, 76, 90)
icon = pygame.transform.scale(pygame.image.load("Assets\Image\Icon.png").convert_alpha(), (32, 32))     #convert alpha use the transparence
background = tools.load_convert("Assets\Image\Room.png")
