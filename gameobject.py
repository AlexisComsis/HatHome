from tools import *

class Game_object:

    defaultimg = []
    defaultimg.append(tools.load("Assets\Image\defaultimg.png"))

    """
    All object in the game
    """
    def __init__(self, x, y, imageup = Game_object.defaultimg[0]):
        self.x = x
        self.y = y
        self.image = image

    def be(self, window):
        window.blit(self.imageup,(self.x, self.y))
