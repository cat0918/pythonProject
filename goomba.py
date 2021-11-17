from pico2d import *
import character

dir=1
dir2=0
death=0
class Goomba():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 105
        self.frame=0
        self.count = 0
        self.image = load_image('monster.png')
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def update(self):
        global dir
        global dir2
        self.frame = (self.frame+0.7) % 8
        if(dir>0):
            self.x += 5
            self.count +=1
            if(self.count>30):
                dir=0
                dir2=1
            if (character.dir > 0):
                if (character.dash > 0):
                    self.x -= 10
                elif (character.dash == 0):
                    self.x -= 5

        elif(dir2>0):
            self.x -= 5
            self.count-=1
            if(self.count<0):
                dir=1
                dir2=0
            if (character.dir3 > 0):
                if (character.dash > 0):

                    self.x += 10
                elif (character.dash == 0):

                    self.x += 5

    def draw(self):
        global dir
        global dir2
        global death
        if (dir2> 0):
            self.image.clip_draw((int)(self.frame) * 120, 0, 120, 105, self.x, self.y, 45, 40)
        elif(dir >0):
            self.image.clip_composite_draw((int)(self.frame) * 120, 0, 120, 105, 0, 'h', self.x, self.y, 45, 40)
        elif(death==1):
            self.image = load_image('goombadeath.png')
            self.image.clip_draw(0, 0, 120, 105, self.x, self.y, 45, 40)


