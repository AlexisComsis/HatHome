import pygame

class Background:

    def __init__(self, speed, image, x, y):
        self.image = image
        self.speed = speed
        self.x = x
        self.y = y

    def be(self, window,  keys):
        self.control(keys)
        window.blit(self.image,(self.x, self.y))

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

    def up(self):
        self.y += self.speed/1.7

    def upleft(self):
        self.y += self.speed /2
        self.x += self.speed /2

    def upright(self):
        self.y += self.speed /2
        self.x -= self.speed /2

    def down(self):
        self.y -= self.speed/1.7

    def downleft(self):
        self.y -= self.speed /2
        self.x += self.speed /2

    def downright(self):
        self.y -= self.speed /2
        self.x -= self.speed /2

    def left(self):
        self.x += self.speed

    def right(self):
        self.x -= self.speed
