from pico2d import *
import character

class Brick():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame =0
        self.side = 0
        self.image = load_image('brick.png')
    def update(self):
        if (character.dir > 0 and self.side == 0):
            if (character.dash > 0):
                self.x -= 10
            elif (character.dash == 0):
                self.x -= 5
        elif (character.dir3 > 0 and self.side == 0):
            if (character.dash > 0):

                self.x += 10
            elif (character.dash == 0):

                self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame, 0, 920, 920, self.x, self.y, 40, 40)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20