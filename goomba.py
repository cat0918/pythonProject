from pico2d import *
import character


dir=1
dir2=0
death=0
smash=0
class Goomba():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 105
        self.frame=0
        self.count = 0
        self.death = 0
        self.image = load_image('monster.png')
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
    def update(self):
        global dir
        global dir2
        global smash
        self.frame = (self.frame+0.7) % 8
        if(dir>0):
            self.x += 5
            self.count += 1
            if(smash==1):
                dir= 0
                dir2 =1
                self.x -=10
                smash=0
            if (character.dir > 0):
                if (character.dash > 0):
                    self.x -= 10
                elif (character.dash == 0):
                    self.x -= 5

        elif(dir2>0):
            self.x -= 5
            self.count-=1
            if(smash==1):
                dir=1
                dir2=0
                self.x +=10
                smash=0
            if (character.dir3 > 0):
                if (character.dash > 0):
                    self.x += 10
                elif (character.dash == 0):
                    self.x += 5

    def draw(self):
        global dir
        global dir2
        if(self.death == 1):
            dir = 0
            dir2 = 0
            self.image = load_image('goombadeath.png')
            self.image.clip_draw(0, 0, 120, 105, self.x, self.y, 45, 40)
        if (dir2> 0):
            self.image.clip_draw((int)(self.frame) * 120, 0, 120, 105, self.x, self.y, 45, 40)
        elif(dir >0):
            self.image.clip_composite_draw((int)(self.frame) * 120, 0, 120, 105, 0, 'h', self.x, self.y, 45, 40)

def collide(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if left_a > right_b: return False
 if right_a < left_b: return False
 if top_a < bottom_b: return False
 if bottom_a > top_b: return False
 return True

