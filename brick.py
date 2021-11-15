from pico2d import *
import character

class Brick():
    def __init__(self):
        self.x = 600
        self.y = 200
        self.frame =0
        self.image = load_image('brick.png')
    def update(self):
        if (character.dir > 0):
            if (character.dash > 0):
                self.x -= 10
            elif (character.dash == 0):
                self.x -= 5
        elif (character.dir3 > 0):
            if (character.dash > 0):

                self.x += 10
            elif (character.dash == 0):

                self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame, 0, 920, 920, self.x, self.y, 45, 40)