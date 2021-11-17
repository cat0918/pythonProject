from pico2d import *
import character
import goomba
import brick
import game_framework
import game_world
import stage1
import start2

image = None
x,y = 0,0
count =0

Block = [ ]
Monster= [ ]

def enter():
    global image
    global curby, monster, block, back,Block, Monster
    curby = character.Curby()
    Block.append(brick.Brick(600,180))
    Block.append(brick.Brick(640,180))
    Block.append(brick.Brick(680,180))
    Monster.append(goomba.Goomba(600,100))
    for i in range(3):
        game_world.add_object(Block[i], 1)
    game_world.add_object(Monster[0], 1)
    back = stage1.Stage()

def update():
    global x
    global y
    global curby, monster, block, back, Block,Monster
    global count
    curby.update()
    for game_object in game_world.all_objects():
        game_object.update()
    back.update()
    delay(0.07)


def draw():
    global image
    global x
    global y
    global curby, monster, block, back,Block,Monster
    clear_canvas()
    back.draw()
    curby.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def handle_events():
    global curby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type, event.key) ==(SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(start2)
        else:
            curby.handle_events(event.type, event.key)



def exit():
    global image
    global curby, monster, block, back, Block,Monster
    del(image)
    del(curby)
    del(Monster)
    del(Block)
    del(back)

def collide(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if left_a > right_b: return False
 if right_a < left_b: return False
 if top_a < bottom_b: return False
 if bottom_a > top_b: return False
 return True