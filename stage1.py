from pico2d import *
import character


class Stage():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('background.png')
    def update(self):
        if (character.dir > 0):
           if (character.dash > 0):
               if(self.x<2400):
                self.x += 10
           elif (character.dash == 0):
               if(self.x<2400):
                self.x += 5
        elif (character.dir3 > 0):
           if (character.dash > 0):
               if (self.x > 0):
                   self.x -= 10

           elif (character.dash == 0):
               if (self.x > 0):
                   self.x -= 5


    def draw(self):
        global dir
        global dir2
        self.image.clip_draw(self.x, self.y, 800 + self.x, 600 + self.y, 400, 300)

