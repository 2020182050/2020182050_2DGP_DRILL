from pico2d import *
import game_framework

class Grass:
    def __init__(self):
        self.image = load_image('img/grass.png')

    def draw(self):
        self.image.draw(400, 30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

grass=None

def enter():
    global grass
    grass = Grass()

def exit():
    global grass
    del grass

def update():
    pass

def draw():
    clear_canvas()
    grass.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass