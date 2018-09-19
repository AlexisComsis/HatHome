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
        window.blit(self.sprite[self.state],(self.x, self.y))

    def move(self):
        Entity.timer1 += rd.randint(1, 50)
        if Entity.timer1 < 6500:
            self.state = 0
        elif Entity.timer1 < 10000:
            self.state = 1
        else:
            Entity.timer1 = 0

class Living(Entity):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Entity.__init__(self, x, y, speed, sprite)
        self.lvl = lvl
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points
