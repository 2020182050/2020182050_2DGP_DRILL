from pico2d import *
import game_framework
import title_state
import play_state
# fill here
# running=True
image =None


def enter():
    global image
    image = load_image('item_select.png')
    # fill here

    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    # logo time을 계산하고, 그결과에 따라 1초가 넘으면 런닝을 false로 변경
    #global logo_time, running
    #delay(0.01)
    #if logo_time >= 1.0:
     #   logo_time = 0.0
     #   game_framework.change_state(title_state)
    #logo_time += 0.01
    # fill here
    play_state.update()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_state.boy.itam = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_state.boy.itam = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_state.boy.itam = 'BigBall'
                    game_framework.pop_state()





