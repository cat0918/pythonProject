from pico2d import *
import character
import goomba
import brick
import game_framework


image = None
x,y = 0,0
count =0

def enter():
    global image
    global curby, monster, block
    image = load_image('background.png')
    curby = character.Curby()
    monster = goomba.Goomba()
    block = brick.Brick()

def update():
    global x
    global y
    global curby, monster, block
    global count
    if(character.dir>0):
        if(character.dash>0):
             x += 10
        elif(character.dash==0):
              x += 5
    elif(character.dir3>0):
        if(character.dash>0):
            if(x>0):
             x-=10
        elif(character.dash==0):
            if(x>0):
             x-=5
    curby.update()
    monster.update()
    block.update()


def draw():
    global image
    global x
    global y
    global dir
    global curby, monster, block
    clear_canvas()
    #image.clip_draw(0,0,1920,1080,0,400)
    image.clip_draw(x, y, 800+x, 600+y, 400, 300)
    curby.draw()
    monster.draw()
    block.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    character.handle_events()
def exit():
    global image
    global curby, monster, block
    del(image)
    del(curby)
    del(monster)
    del(block)