from pico2d import *
import character
import goomba
import brick
import game_framework
import game_world2
import stage2
import pipe
import trap
import star
import flag
import rocket
import gameover
import gameclear
from list2 import *

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
    curby.f = 200
    flag.clear = 0
    block()
    tunnel()
    Ro.append(rocket.Rocket(800,350))
    Flag.append(flag.Flag(2400, 350))
    Spike.append(trap.Trap(860,180))
    Spike.append(trap.Trap(890,180))
    Spike.append(trap.Trap(920,180))
    Spike.append(trap.Trap(950,180))
    Spike.append(trap.Trap(980,180))
    Spike.append(trap.Trap(1010,180))
    Spike.append(trap.Trap(1040,180))
    Spike.append(trap.Trap(1070,180))
    Spike.append(trap.Trap(1160,180))
    Spike.append(trap.Trap(1190,180))
    Spike.append(trap.Trap(1220,180))
    Spike.append(trap.Trap(1250,180))
    Spike.append(trap.Trap(1280,180))
    Spike.append(trap.Trap(1310,180))
    Spike.append(trap.Trap(1340,180))
    Spike.append(trap.Trap(1370,180))
    Spike.append(trap.Trap(1400,180))
    Spike.append(trap.Trap(1430,180))
    Spike.append(trap.Trap(1460,180))
    Spike.append(trap.Trap(1490,180))
    Star.append(star.Star(1460,500))
    for i in range(3):
        game_world2.add_object(Tunnel[i], 1)
    for i in range(22):
        game_world2.add_object(Block[i],1)
    game_world2.add_object(Flag[0],1)
    game_world2.add_object(Star[0],1)
    game_world2.add_object(Ro[0],1)
    for i in range(20):
     game_world2.add_object(Spike[i],1)
    #for i in range(4):
        #game_world2.add_object(Spike[i],1)

def update():
    global x
    global y
    global curby, monster, block, back, Block, Tunnel
    global count
    curby.update()
    back.update()
    for i in range(22):
        if (collide(curby, Block[i]) == 2):
            print(curby.floor)
            curby.floor = Block[i].y + 45
            print(curby.floor)
            curby.crash = 1
            # print(Block[i].y)
            # print(curby.y)
        elif (collide(curby, Block[i]) == 1):
            curby.count = 11
    for i in range(3):
        if(collide(curby,Tunnel[i]) == 2):
            curby.floor = Tunnel[i].y+60
            curby.crash = 1
    if(collide(curby,Ro[0])):
        game_framework.change_state(gameover)
    elif (collide(curby, Star[0])):
        game_world2.remove_object(Star[0])
    elif (collide(curby, Flag[0])):
        game_framework.change_state(gameclear)
    for game_object in game_world2 .all_objects():
        game_object.update()

    delay(0.06)


def draw():
    global image
    global x
    global y
    global curby, monster, block, back, Block, Tunnel
    clear_canvas()
    back.draw()
    curby.draw()
    for game_object in game_world2.all_objects():
        game_object.draw()
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
    global curby, monster, block, back, Tunnel,Spike
    del(image)
    del(curby)
    del(back)

def block():
    global Block
    Block.append(brick.Brick(580, 280))
    Block.append(brick.Brick(620, 280))
    Block.append(brick.Brick(660, 280))

    Block.append(brick.Brick(1200,280))
    Block.append(brick.Brick(1240,280))
    Block.append(brick.Brick(1280,280))
    Block.append(brick.Brick(1320,280))
    Block.append(brick.Brick(1360,280))
    Block.append(brick.Brick(1400,280))
    Block.append(brick.Brick(1440,280))
    Block.append(brick.Brick(1480,280))
    Block.append(brick.Brick(1520,280))
    Block.append(brick.Brick(1560,280))
    Block.append(brick.Brick(1600,280))
    Block.append(brick.Brick(1640,280))
    Block.append(brick.Brick(1680,280))

    Block.append(brick.Brick(1320, 400))
    Block.append(brick.Brick(1360, 400))
    Block.append(brick.Brick(1400, 400))
    Block.append(brick.Brick(1440, 400))
    Block.append(brick.Brick(1480, 400))
    Block.append(brick.Brick(1520, 400))




def tunnel():
    global Tunnel
    Tunnel.append(pipe.Pipe(800, 200))
    Tunnel.append(pipe.Pipe(1100, 200))
    Tunnel.append(pipe.Pipe(1800, 200))


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
