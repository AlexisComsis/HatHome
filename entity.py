
class Entity:

    def __init__(self, x, y, speed, sprite):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite

    def display(self, window):
        window.blit(self.sprite[self.direction],(self.x, self.y))


class Living(Entity):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Entity.__init__(self, x, y, speed, sprite)
        self.lvl = lvl
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points

class Player(Living):

    def __init__(self, x, y, speed, sprite, hp_limit, lvl):
        Living.__init__(self, x, y, speed, sprite, hp_limit, lvl)
        self.direction = 0


    #0 = front
    #1 = right1
    #2 = right2
    #3 = left1
    #4 = left2
    #5 = down1
    #6 = down2
    #7 = up1
    #8 = up2
    #9 = upright1
    #10 = upright2
    #11 = upleft1
    #12 = upleft2
    #13 = downright1
    #14 = downright2
    #15 = downleft1
    #16 = downleft2

    timer1 = 0

    def movement(self,spr1,spr2):
        Player.timer1 += 1

        if Player.timer1 <= 7:
            self.direction = spr1
        elif Player.timer1 <= 14:
            self.direction = spr2
        else:
            Player.timer1 = 0

    def up(self):
        self.y -= self.speed
        Player.timer1 += 1
        self.movement(7,8)

    def upleft(self):
        self.y -= self.speed /1.5
        self.x -= self.speed /1.5
        self.movement(11,12)

    def upright(self):
        self.y -= self.speed /1.5
        self.x += self.speed /1.5
        self.movement(9,10)

    def down(self):
        self.y += self.speed
        self.movement(5,6)

    def downleft(self):
        self.y += self.speed /1.5
        self.x -= self.speed /1.5
        self.movement(15,16)

    def downright(self):
        self.y += self.speed /1.5
        self.x += self.speed /1.5
        self.movement(13,14)

    def left(self):
        self.x -= self.speed
        self.movement(3,4)

    def right(self):
        self.x += self.speed
        self.movement(1,2)
