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

image = None
x,y = 0,0
count =0
starcount=0


Block = [ ]
Monster= [ ]
Tunnel = [ ]
Star = [ ]
Flag = [ ]

def enter():
    global image
    global curby, monster, block, back,Block, Monster,Tunnel, Star, Flag
    curby = character.Curby()
    block()
    Monster.append(goomba.Goomba(800,100))
    Tunnel.append(pipe.Pipe(800,100))
    Tunnel.append(pipe.Pipe(1100,100))
    Tunnel.append(pipe.Pipe(1800,100))
    Tunnel.append(pipe.Pipe(1880,100))
    Tunnel.append(pipe.Pipe(1960,100))
    Star.append(star.Star(1420,100))
    Flag.append(flag.Flag(2600,250))
    for i in range(22):
        game_world.add_object(Block[i], 1)
    game_world.add_object(Monster[0], 1)
    game_world.add_object(Star[0], 1)
    game_world.add_object(Flag[0], 1)
    for i in range(5):
     game_world.add_object(Tunnel[i], 1)
    back = stage1.Stage()

def update():
    global x
    global y
    global curby, monster, block, back, Block,Monster,Tunnel,Star
    global count
    global starcount
    left_b, bottom_b, right_b, top_b = Block[0].get_bb()
    for i in range(22):
     if(collidetest(curby,Block[i])):
         curby.y = Block[i].y+20
         curby.crash = 1


    if(collide(curby, Star[0])):
        game_world.remove_object(Star[0])
        starcount += 1
        print(starcount)

    curby.update()
    for game_object in game_world.all_objects():
        game_object.update()
    back.update()
    if (collide(curby, Flag[0])):
        print(starcount)
        if (starcount > 1):
            flag.clear = 1
            count += 1
            print(count)
            if(count>7):
             game_framework.change_state(start2)
    delay(0.07)


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
    global curby, monster, block, back, Block,Monster,Tunnel
    del(image)
    del(curby)
    del(Monster)
    del(Block)
    del(back)
    del(Tunnel)

def collide(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if left_a > right_b: return False
 if right_a < left_b: return False
 if top_a < bottom_b: return False
 if bottom_a > top_b: return False
 return True
def collidetest(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if bottom_a >top_b  and left_a > left_b and left_a < right_b: return True
 if bottom_a>top_b  and right_a>left_b and right_a < right_b: return True


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

    Block.append(brick.Brick(2200, 80))
    Block.append(brick.Brick(2240, 80))
    Block.append(brick.Brick(2280, 80))
    Block.append(brick.Brick(2320, 80))

    Block.append(brick.Brick(2240, 120))
    Block.append(brick.Brick(2280, 120))
    Block.append(brick.Brick(2320, 120))

    Block.append(brick.Brick(2280, 160))
    Block.append(brick.Brick(2320, 160))

    Block.append(brick.Brick(2320, 200))
