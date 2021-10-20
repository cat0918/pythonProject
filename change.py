from pico2d import *

c = 0
cha = 0


def update():
    global c
    global cha
    if (c == 0):
        cha = 0
    elif (c == 1):
        cha = 1
