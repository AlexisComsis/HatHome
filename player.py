from entity import*

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

    def control(self, keys):
        #UP
        if keys[pygame.K_w]:
            if keys[pygame.K_a]:
                self.upleft()
            elif keys[pygame.K_d]:
                self.upright()
            else:
                self.up()

        #DOWN
        elif keys[pygame.K_s]:
            if keys[pygame.K_a]:
                self.downleft()
            elif keys[pygame.K_d]:
                self.downright()
            else:
                self.down()

        #LEFT
        elif keys[pygame.K_a]:
            self.left()

        #RIGHT
        elif keys[pygame.K_d]:
            self.right()



    def movement(self,spr1,spr2):
        Player.timer1 += 1

        if Player.timer1 <= 7:
            self.direction = spr1
        elif Player.timer1 <= 14:
            self.direction = spr2
        else:
            Player.timer1 = 0

    def up(self):
        self.y -= self.speed/1.7
        Player.timer1 += 1
        self.movement(7,8)

    def upleft(self):
        self.y -= self.speed /2
        self.x -= self.speed /2
        self.movement(11,12)

    def upright(self):
        self.y -= self.speed /2
        self.x += self.speed /2
        self.movement(9,10)

    def down(self):
        self.y += self.speed/1.7
        self.movement(5,6)

    def downleft(self):
        self.y += self.speed /2
        self.x -= self.speed /2
        self.movement(15,16)

    def downright(self):
        self.y += self.speed /2
        self.x += self.speed /2
        self.movement(13,14)

    def left(self):
        self.x -= self.speed
        self.movement(3,4)

    def right(self):
        self.x += self.speed
        self.movement(1,2)
