from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir_x
    global dir_y
    global line
    stand = 300
    stand_left = 200
    run = 100
    run_left = 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                if dir_x == 1:
                    line = run
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                if dir_x == -1:
                    line = run_left
            elif event.key == SDLK_UP:
                dir_y += 1
                if dir_x  < 0 or line == stand_left:
                    line = run_left
                else:
                    line = run
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                if dir_x  < 0 or line == stand_left:
                    line = run_left
                else:
                    line = run
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                if dir_y == 0:
                    line = stand
            elif event.key == SDLK_LEFT:
                dir_x += 1
                if dir_y == 0:
                    line = stand_left
            elif event.key == SDLK_UP:
                dir_y -= 1
                if dir_x == 0:
                    line = stand
            elif event.key == SDLK_DOWN:
                dir_y += 1
                if dir_x == 0:
                    line = stand

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
line = 300


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, line, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y * 5

    delay(0.02)

close_canvas()

