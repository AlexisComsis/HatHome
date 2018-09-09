
class Entity:

    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite

    def display(self, window):
        window.blit(self.sprite[4],(self.x, self.y))


class Living(Entity):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Entity.__init__(self, x, y, speed, sprite)
        self.lvl = lvl
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points

class Player(Living):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Living.__init__(self, x, y, speed, sprite, hp_limit, lvl)

    def up(self):
        self.y -= self.speed
    def down(self):
        self.y += self.speed
    def left(self):
        self.x -= self.speed
    def right(self):
        self.x += self.speed
