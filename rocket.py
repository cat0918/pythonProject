from pico2d import *
import character

class Rocket():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame =0
        self.side = 0
        self.image = load_image('rocket.png')
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
        self.x -=10
        if(self.x <0):
            self.x = 800

    def draw(self):
        self.image.clip_draw(self.frame, 0, 225, 225, self.x, self.y, 50, 40)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 25, self.y - 15, self.x + 25, self.y + 15