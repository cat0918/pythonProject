from pico2d import *
import character
image = None
x,y = 0,0
count =0
def enter():
    global image
    image = load_image('background.png')

def update():
    global x
    global y
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

def draw():
    global image
    global x
    global y
    global dir
    clear_canvas()
    #image.clip_draw(0,0,1920,1080,0,400)
    image.clip_draw(x, y, 800+x, 600+y, 400, 300)
    update_canvas()