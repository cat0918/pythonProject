from pico2d import *
import start
import character
import goomba
import title
import brick
import change

running = True
change =19


open_canvas()
curby = character.Curby()
monster = goomba.Goomba()
block = brick.Brick()


def collide(a, b):
 left_a, bottom_a, right_a, top_a = a.get_bb()
 left_b, bottom_b, right_b, top_b = b.get_bb()
 if left_a > right_b: return False
 if right_a < left_b: return False
 if top_a < bottom_b: return False
 if bottom_a > top_b: return False
 return True


while running:
 start.enter()
 title.enter()
 character.handle_events()
 curby.update()
 block.update()
 monster.update()
 start.update()
 clear_canvas()
 if(change ==0):
  title.draw()
 elif(change !=0):
  start.draw()
 curby.draw()
 block.draw()
 monster.draw()
 update_canvas()


close_canvas()