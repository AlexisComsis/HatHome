from player import *

class Movemap:

        def package_move(player_object, object, keys):


        def updater_speed(player_object):
            player_object.speed = speed0

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

        r = 2
        p = 1.7

        def up(self):
            self.y += self.speed0/p

        def upleft(self):
            self.y += self.speed0 /r
            self.x += self.speed0 /r

        def upright(self):
            self.y += self.speed0 /r
            self.x -= self.speed0 /r

        def down(self):
            self.y -= self.speed0/p

        def downleft(self):
            self.y -= self.speed0 /r
            self.x += self.speed0 /r

        def downright(self):
            self.y -= self.speed0 /r
            self.x -= self.speed0 /r

        def left(self):
            self.x += self.speed0

        def right(self):
            self.x -= self.speed0

        def control(object, keys):

            #UP
            if keys[pygame.K_w]:
                if keys[pygame.K_a]:
                    object.upleft()
                elif keys[pygame.K_d]:
                    object.upright()
                else:
                    object.up()

            #DOWN
            elif keys[pygame.K_s]:
                if keys[pygame.K_a]:
                    object.downleft()
                elif keys[pygame.K_d]:
                    object.downright()
                else:
                    object.down()

            #LEFT
            elif keys[pygame.K_a]:
                object.left()

            #RIGHT
            elif keys[pygame.K_d]:
                object.right()
