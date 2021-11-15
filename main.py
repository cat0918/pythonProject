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