'''
load the images etc...
'''
from tools import *

HomeSprite = tools.separate("Assets\Image\HomeSprite.png", 26, 30)
Icon = []
Icon.append(pygame.transform.scale(pygame.image.load("Assets\Image\Icon.png").convert_alpha(), (48, 48)))     #convert alpha use the transparence
