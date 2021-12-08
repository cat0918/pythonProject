from pico2d import *
import character
import goomba
import brick
import game_framework
import game_world
import stage1
import start2
import pipe
import star
import flag
from list import *

image = None
x,y = 0,0
count =0
starcount=0




def enter():
    global image
    global curby, monster, block, back,Block, Monster,Tunnel, Star, Flag
    curby = character.Curby()
    monster = goomba.Goomba(x,y)
    block()
    #Monster.append(goomba.Goomba(800,100))
    Tunnel.append(pipe.Pipe(1000,100))
    Tunnel.append(pipe.Pipe(1800,100))
    Tunnel.append(pipe.Pipe(2100,100))
    Star.append(star.Star(1420,400))
    Star.append(star.Star(2000,100))
    Flag.append(flag.Flag(2600,250))
    for i in range(15):
        game_world.add_object(Block[i], 1)
    #game_world.add_object(Monster[0], 1)
    for i in range(2):
     game_world.add_object(Star[i], 1)
    game_world.add_object(Flag[0], 1)
    for i in range(3):
     game_world.add_object(Tunnel[i], 1)
    back = stage1.Stage()

def update():
    global x
    global y
    global curby, monster, block, back, Block,Monster,Tunnel,Star
    global count
    global starcount
    left_b, bottom_b, right_b, top_b = Block[0].get_bb()
    for i in range(15):
     if(collide(curby,Block[i]) == 2):
         print(curby.floor)
         curby.floor = Block[i].y + 45
         print(curby.floor)
         curby.crash = 1
         #print(Block[i].y)
         #print(curby.y)
     elif(collide(curby, Block[i]) == 1):
         curby.count = 11

     #elif(collide(curby,Block[i])):
         #curby.count = 11
    for i in range(3):
        if(collide(curby,Tunnel[i]) == 2):
            curby.floor = Tunnel[i].y+60
            curby.crash = 1
        elif(collide(curby,Tunnel[i]) == 1):
            print(123)
            #back.side = 1
    for i in range(2):
     if(collide(curby, Star[i])):
         game_world.remove_object(Star[i])
         starcount += 1


    curby.update()
    for game_object in game_world.all_objects():
        game_object.update()
    back.update()
    if (collide(curby, Flag[0])):
        if (starcount > 1):
            flag.clear = 1
            count += 1
            if(count>7):
             game_framework.change_state(start2)
             game_world.clear()
    delay(0.06)


def draw():
    global image
    global x
    global y
    global curby, monster, block, back,Block,Monster,Tunnel
    clear_canvas()
    back.draw()
    curby.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def handle_events():
    global curby, Block, Star, Tunnel
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type, event.key) ==(SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(start2)
            game_world.clear()
            print(1)

        else:
            curby.handle_events(event.type, event.key)



def exit():
    global image
    global curby, monster, block, back, Block,Monster,Tunnel
    del(image)
    del(curby)
    Block.clear()
    Tunnel.clear()
    print(1)

    del(back)

def collide(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if left_a > right_b: return 0
 if right_a < left_b: return 0
 if top_a < bottom_b: return 0
 if bottom_a > top_b: return 0

 if bottom_a < top_b:
     #print(321)
     if bottom_a+20> top_b:
         #print(123)
         return 2
 return 1

def collidetest(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if bottom_a >top_b-5 and bottom_a<top_b+10  and left_a > left_b and left_a < right_b: return True
 if bottom_a>top_b-5 and bottom_a<top_b+10< right_a>left_b and right_a < right_b: return True

 return False


def block():
    global Block
    Block.append(brick.Brick(600, 180))
    Block.append(brick.Brick(640, 180))
    Block.append(brick.Brick(680, 180))
    Block.append(brick.Brick(1220, 180))
    Block.append(brick.Brick(1260, 180))
    Block.append(brick.Brick(1300, 180))
    Block.append(brick.Brick(1380, 300))
    Block.append(brick.Brick(1420, 300))
    Block.append(brick.Brick(1460, 300))
    Block.append(brick.Brick(1540, 180))
    Block.append(brick.Brick(1580, 180))
    Block.append(brick.Brick(1620, 180))

    Block.append(brick.Brick(2000, 180))
    Block.append(brick.Brick(1960, 180))
    Block.append(brick.Brick(2040, 180))


