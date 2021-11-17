from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, JUMP_STOP, UP_UP =range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}
class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 7
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw((boy.frame) * 45, 360, 45, 40, boy.x, boy.y)
        else:
            boy.image.clip_composite_draw((boy.frame) * 45, 360, 45, 40, 0, 'h', boy.x, boy.y, 45, 40)
class Jumpstate:
    def enter(boy, event):

        if event == UP_DOWN:
            boy.velocity += 1
        boy.timer = 300
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = 0
        boy.timer -= 1
        if(boy.timer>0):
         boy.y += boy.velocity
        else:
         boy.y -=boy.velocity
         if(boy.y<100):
             boy.add_event(JUMP_STOP)
             boy.velocity=0

    def draw(boy):
        boy.image.clip_draw((boy.frame)*45, 280, 45,40,boy.x,boy.y)
class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = int((boy.frame + 0.1)) % 2
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 45, 240, 45, 40, boy.x, boy.y)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 45, 240, 45, 40, 0, 'h', boy.x, boy.y, 45, 40)

next_state_table = {
IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN:Jumpstate},
RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState},
Jumpstate: {JUMP_STOP: IdleState, UP_UP: Jumpstate, RIGHT_DOWN: RunState, LEFT_DOWN: RunState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 100
        self.image = load_image('curby.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        pass


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)
        pass


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir))



    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        pass

