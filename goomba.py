from pico2d import *

class Goomba():
    def __init__(self):
        self.x = 600
        self.y = 100
        self.h = 360
        self.frame=0
        self.count = 0
        self.image = load_image('monster.png')
    def update(self):
        global dir
        global dir2
        self.frame = (self.frame+0.7) % 8

    def draw(self):

