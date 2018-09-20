from entity import *

class Living(Entity):

    def __init__(self, x, y, image, hp_limit, speed):
        Entity.__init__(self, x, y, image)
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points
        self.speed = speed

    def updater(self):
        pass
