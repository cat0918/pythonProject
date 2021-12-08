from pico2d import *
import game_framework
import start

name = 'titlestate'
image = None
logo_time =0.0

def enter():
    global image
    image = load_image('gameclear.png')

def update():
    global logo_time


    logo_time += 0.01
def draw():
    global image
    clear_canvas()
    image.clip_draw(0,0,1280,720,400,300,800,600)
    update_canvas()
def handle_events():
 events = get_events()
 for event in events:
     if event.type == SDL_QUIT:
         game_framework.quit()
     else:
         if(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
             game_framework.change_state(start)

def exit():
    global image
    del(image)

