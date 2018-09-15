from tools import *

class Entity:

    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed /1600 * tools.w0
        self.sprite = sprite

    def display(self, window):
        window.blit(self.sprite[self.direction],(self.x, self.y))


class Living(Entity):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Entity.__init__(self, x, y, speed, sprite)
        self.lvl = lvl
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points
