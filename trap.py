from pico2d import *
import character

class Trap():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame =0
        self.image = load_image('trap.png')
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
        self.image.clip_draw(self.frame, 0, 839, 900, self.x, self.y, 30, 30)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15