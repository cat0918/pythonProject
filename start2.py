from pico2d import *
import character
import goomba
import brick
import game_framework
import stage2

image = None
x,y = 0,0
count =0

def enter():
    global image
    global curby, monster, block, back, Block, Monster, Tunnel, Star, Flag
    curby = character.Curby()
    back = stage2.Stage2()
    curby.y = 200
    curby.floor = 200

def update():
    global x
    global y
    global curby, monster, block, back
    global count
    curby.update()
    back.update()

    delay(0.1)


def draw():
    global image
    global x
    global y
    global curby, monster, block, back
    clear_canvas()
    back.draw()
    curby.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            curby.handle_events(event.type, event.key)



def exit():
    global image
    global curby, monster, block, back
    del(image)
    del(curby)
    del(back)