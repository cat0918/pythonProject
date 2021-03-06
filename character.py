from pico2d import *
import game_world

class Curby():
 def __init__(self):
  self.x, self.y = 400, 100
  self.h = 360
  self.frame = 0
  self.count = 0
  self.crash = 0
  self.fall = 0
  self.floor= 100
  self.stop = 0
  self.f=100
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
    self.y -= dir2 * 15
    if (self.y < self.floor):
     dir2 = 0
     print(self.floor)
     self.y = self.floor
     print(self.y)
     self.count = 0
   if(self.crash ==1):
    dir2 = 0
    self.y = self.floor
    self.count = 0
    self.crash = 0
    self.floor = self.f

  if dir==0 and dir3==0 and dir2 == 0:
   self.h = 240
   self.frame = (self.frame + 0.1) % 2
  if self.stop == 1:
   dir = 0
 def draw(self):
  if(dir>0):
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
  elif(dir3>0):
   self.image.clip_composite_draw((int)(self.frame) * 45, self.h, 45, 40 ,0,'h', self.x, self.y,45,40)
  elif(dir2>0):
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
  elif dir==0 and dir3==0:
   self.image.clip_draw((int)(self.frame) * 45, self.h, 45, 40, self.x, self.y)
  draw_rectangle(*self.get_bb())
 def get_bb(self):
  return self.x-20, self.y-20,self.x+20, self.y+20
 def handle_events(self, eventtype, eventkey):
  global running
  global frame
  global x
  global dir
  global dir2
  global dir3
  global dash
  if eventtype == SDL_KEYDOWN:
   if eventkey == SDLK_RIGHT:
    dir +=1
   elif eventkey == SDLK_LEFT:
    dir3 +=1
   elif eventkey == SDLK_UP:
    dir2 += 1
   elif eventkey == SDLK_e:
    dash +=1
  elif eventtype == SDL_KEYUP:
   if eventkey == SDLK_RIGHT:
    dir -=1
   elif eventkey == SDLK_LEFT:
    dir3 -=1
   elif eventkey == SDLK_e:
    dash -=1


dir = 0
dir2 = 0
dir3 = 0
dash =0