from pico2d import *
open_canvas()
character = load_image('penguin.png')

frame = 0
line = 128
ghost_attack = line*5
walk_right = line*15
draw_circle = line*12
walk_back = line*10
jump = line*6

def use_sprite(x,y,what,cnt):
    global frame
    clear_canvas()
    character.clip_draw((frame *128),what,128,128,x,y)
    update_canvas()
    frame = (frame+1)%cnt
    delay(0.05)
    get_events()

x = 50
while(1):
    for n in range(0,16*4):
        use_sprite(400,300,ghost_attack,16)
    
    for x in range(50,751,5):
        use_sprite(x,64,walk_right,9)
    
    for n in range(0,8*4):
        use_sprite(750,64,draw_circle,8)
    
    for n in range(0,6*10):
        use_sprite(750,64,walk_back,6)
    
    for n in range(0,12*10):
        use_sprite(750,64,jump,12)


close_canvas()