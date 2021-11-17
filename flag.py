from pico2d import *
import character

clear = 0
class Flag():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame =0
        self.image = load_image('flag.png')
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
        global clear
        if(clear ==0):
         self.image.clip_draw(self.frame, 0, 900, 2062, self.x, self.y, 200, 400)
        else:
         self.image = load_image('clear.png')
         self.image.clip_draw(self.frame, 0, 900, 2062, self.x, self.y, 200, 400)
    def get_bb(self):
        return self.x - 70, self.y - 200, self.x + 70, self.y + 200