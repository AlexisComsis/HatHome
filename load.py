'''
load the images etc...
'''
from tools import *

spriteplayer = tools.separate("HatHome\Assets\Image\SpritePlayer.png", 78)
icon = pygame.transform.scale(pygame.image.load("HatHome\Assets\Image\Icon.png").convert_alpha(), (32, 32))     #convert alpha use the transparence
background = tools.load_convert("HatHome\Assets\Image\Room.png")
background = pygame.transform.scale(background.convert_alpha(), (tools.w0, tools.h0))
textbox = tools.load_convert("HatHome\Assets\Image\Textbox.png")
spriteservietsky = tools.separate("HatHome\Assets\Image\SpriteServietsky.png", 78)
