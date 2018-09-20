from tools import *
import random as rd

class Entity:



    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed /1600 * tools.w0
        self.sprite = sprite
        self.state = 0

    timer1 = 0

    def display(self, window):
        self.updater()
        window.blit(self.sprite[self.state],(self.x, self.y))

    def updater(self):
        Entity.timer1 += 1
        if Entity.timer1 < 65:
            self.state = 0
        elif Entity.timer1 < 90:
            self.state = 1
        else:
            Entity.timer1 = 0

class Living(Entity):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Entity.__init__(self, x, y, speed, sprite)
        self.lvl = lvl
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points
