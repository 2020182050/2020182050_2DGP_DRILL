import random
from pico2d import *
import server
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y= random.randint(0, server.background.w), random.randint(0, server.background.h)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
