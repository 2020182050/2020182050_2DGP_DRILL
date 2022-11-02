from pico2d import *

#2.이벤트 정의
RD, LD, RU, LU, TIMER, aD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT)  : LD,
    (SDL_KEYUP, SDLK_RIGHT)   : RU,
    (SDL_KEYUP, SDLK_LEFT)    : LU,
    (SDL_KEYDOWN, SDLK_a) : aD
}

#1.상태정의
class IDLE:
    def enter(self, event): #상태에 들어갈 떄 행하는 액션
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    def exit(self): #상태를 나올 떄 행하는 액션
        print('EXIT IDLE')

    def do(self): #상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    def enter(self, event): #상태에 들어갈 떄 행하는 액션
        print('ENTER RUN')  
        #어떤 키가 눌렸는지에 따라 방향판단
        #키 이벤트 정보가 필요
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self): #상태를 나올 떄 행하는 액션
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self): #상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
    
class SLEEP:
    def enter(self, event): #상태에 들어갈 떄 행하는 액션
        print('ENTER SLEEP')

    def exit(self): #상태를 나올 떄 행하는 액션
        print('EXIT SLEEP')

    def do(self): #상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
            -3.141592/2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
            3.141592/2, '', self.x + 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event): #상태에 들어갈 떄 행하는 액션
        print('ENTER AUTO_RUN')
        if self.face_dir == 1:
            self.dir = 1
        else:
            self.dir = -1

    def exit(self): #상태를 나올 떄 행하는 액션
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0

    def do(self): #상태에 있을 때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        if self.x > 760 :
            self.dir = -1
        elif self.x < 40:
            self.dir = 1
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 40, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 40, 200, 200)

#3.상태 변환 기술
next_state = {
    IDLE : {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, aD: AUTO_RUN},
    RUN  : {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, aD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, aD: SLEEP},
    AUTO_RUN:{RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN, LD: RUN, aD: AUTO_RUN}
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
    
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.event_que.insert(0, key_event)

    def add_event(self, event):
        self.event_que.insert(0,event)

