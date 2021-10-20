from pico2d import *
import change
image = None

image = None

def enter():
    global image
    image = load_image('title.jpg')

def draw():
    global image
    clear_canvas()
    image.clip_draw(0,0,1280,720,400,300,800,600)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                change.c = 1

