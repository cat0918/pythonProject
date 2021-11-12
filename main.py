from pico2d import *
import start
import character
import title
import change

running = True
change =19


open_canvas()
curby = character.Curby()

while running:
 start.enter()
 title.enter()
 character.handle_events()
 curby.update()
 start.update()
 clear_canvas()
 if(change ==0):
  title.draw()
 elif(change !=0):
  start.draw()
 curby.draw()
 update_canvas()


close_canvas()