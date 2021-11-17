from pico2d import *
import character

class Star():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame =0
        self.image = load_image('star.png')
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
        self.image.clip_draw(self.frame, 0, 348, 346, self.x, self.y, 60, 60)
    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30