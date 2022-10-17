from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

boy=None #None==NULL
grass=None
running=True

open_canvas()

#Init
def enter():
    global boy
    global grass
    global running
    boy = Boy()
    grass = Grass()
    running = True

#finish
def exit():
    global boy, grass
    del boy
    del grass

#world object update
def update():
    boy.update()

#render world
def render():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

enter()
# game main loop code
while running:
    handle_events()
    update()
    render()
    delay(0.05)

exit()
# finalization code
close_canvas()
