from pico2d import *
import game_framework
import logo_state
import title_state
import itam_state
import add_del_boy_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.itam = None
        self.ball = load_image('ball21x21.png')
        self.bigball = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.itam == 'Ball':
            self.ball.draw(self.x+10,self.y+50)
        elif self.itam == 'BigBall':
            self.bigball.draw(self.x + 10, self.y + 50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(itam_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_del_boy_state)


boy=None #None==NULL
grass=None
team = []
# running=True

open_canvas()

#Init
def enter():
    global boy
    global grass
    # global running
    boy = Boy()
    grass = Grass()
    # running = True

#finish
def exit():
    global boy, grass
    del boy
    del grass

#world object update
def update():
    boy.update()
    for boy_team in team:
        boy_team.update()

#render world
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    boy.draw()
    for boy_team in team:
        boy_team.draw()

def pause():
    pass

def resume():
    pass

