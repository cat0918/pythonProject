from pico2d import *
import game_world

class Curby():
 def __init__(self):
  self.x, self.y = 400, 100
  self.h = 360
  self.frame = 0
  self.count = 0
  self.image = load_image('curby.png')
 def update(self):
  global dir
  global dir2
  if (dir > 0):
   if(dash>0):
    self.h = 320
    self.frame = (self.frame + 0.7) % 7
    #self.x += dir * 10
   elif(dash==0):
    self.h = 360
    self.frame = (self.frame + 0.7) % 7
    #self.x += dir * 5
  if(dir3>0):
   if (dash > 0):
    self.h =  320
    self.frame = (self.frame + 0.7) % 7
    #if(45<=self.x<=400):
     #self.x -= dir3 * 10
   elif (dash == 0):
    self.h = 360
    self.frame = (self.frame + 0.7) % 7
    #if(45<=self.x<=400):
     #self.x -= dir3 * 5
  if (dir2 > 0):
   self.h = 280
   self.count += 1
   self.frame = 0
   if (self.count < 10):
    self.frame = 0
    self.y += dir2 * 20
   elif (self.count > 10):
    self.frame = 1
    self.count -= 1
    self.y -= dir2 * 30
    if (self.y < 100):
     dir2 = 0
     self.count = 0
  if dir==0 and dir3==0 and dir2 == 0:
   self.h = 240
   self.frame = (self.frame + 0.1) % 2
 def draw(self):
  if(dir>0):
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
  elif(dir3>0):
   self.image.clip_composite_draw((int)(self.frame) * 45, self.h, 45, 40 ,0,'h', self.x, self.y,45,40)
  elif(dir2>0):
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
  elif dir==0 and dir3==0:
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
 def get_bb(self):
  return self.x-20, self.y-20,self.x+20, self.y+20
def handle_events():
 global running
 global frame
 global x
 global dir
 global dir2
 global dir3
 global dash
 events = get_events()
 for event in events:
  if event.type == SDL_KEYDOWN:
   if event.key == SDLK_RIGHT:
    dir +=1
   elif event.key == SDLK_UP:
    dir2 +=1
   elif event.key == SDLK_LEFT:
    dir3 += 1
   elif event.key == SDLK_e:
    dash +=1
  elif event.type == SDL_KEYUP:
   if event.key == SDLK_RIGHT:
    dir -= 1
   elif event.key == SDLK_LEFT:
    dir3 -=1
   elif event.key == SDLK_e:
    dash -=1


dir = 0
dir2 = 0
dir3 = 0
dash =0