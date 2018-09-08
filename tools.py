'''
Tools for the developpement
'''
import json
import pygame

class tools:

    # take the height and width needed
    with open("Assets\Data\Options.txt", "r+") as openfile:
        openfile = json.loads(openfile.read())
        w0 = openfile["Width"]
        h0 = openfile["Height"]

    # Convert resolution depending on the screen
    def convert_coord(nx, ny, w=w0, h=h0):
        return [int(nx / 1600 * w), int(ny / 900 * h)]

    # Possibly usefull find the width and height of an image
    def get_width(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        return img.get_width()
    def get_height(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        return img.get_height()

    def lc(img_path, w=w0, h=h0):   #lc for load convert
        img = pygame.image.load(img_path).convert_alpha()
        wc = int(img.get_width() / 1600 * w)
        hc = int(img.get_height() / 900 * h)
        return pygame.transform.scale(img, (wc, hc))

    def give(file, key, cat, value):
        with open("Data"+file, "r") as options:
            data = options.read()
            options = json.loads(data)

            (options[key][cat]) = value
            data = json.dumps(options)

        with open("Data"+file, "w") as file:
            file.write(data)

    def separate(img_path, x, y, w=w0, h=h0):
        '''
        separate different sprites
        '''
        img = tools.lc(img_path)
        converted_sizer = tools.convert_coord(x, y)
        timer = int(img.get_width() / converted_sizer[0])
        img_list = list()
        for i in range(0, timer):
            img_list.append(img.subsurface(i * converted_sizer[0], 0, converted_sizer[0], converted_sizer[1]))
        return img_list
