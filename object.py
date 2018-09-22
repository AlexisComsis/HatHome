import pygame

class Object:

    defaultimage = []
    defaultimage.append(pygame.image.load("Assets/Image/Defaultimage.png").convert_alpha())

    def __init__(self, x=0, y=0, imageup=defaultimage[0], image_bank=defaultimage):
        self.x = x
        self.y = y
        self.imageup = imageup
        self.image_bank = defaultimage
