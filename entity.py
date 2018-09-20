from tools import *

class Entity:
    """
    All entity who get an x and y and can be
    """
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def be(self, window):
        window.blit(self.image,(self.x, self.y))
