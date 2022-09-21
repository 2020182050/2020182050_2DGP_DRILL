from pico2d import *
from math import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400,30)
#character.draw_now(400,90)

while (1):
    x = 400
    y = 90
    case = 1
    rad = -90
    while (x <= 780 and case == 1):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)

        x += 2
        delay(0.01)
        if (x == 780):
            case += 1
            x -= 2
    
    while (y <= 570 and case == 2):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(780,y)

        y += 4
        delay(0.01)
        if (y == 570):
            case += 1
            y -= 4
    
    while (x >= 20 and case == 3):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,570)

        x -= 2
        delay(0.01)
        if (x == 20):
            case += 1
            x += 2
    
    while (y >= 90 and case == 4):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(20,y)

        y -= 4
        delay(0.01)
        if (y == 90):
            case += 1
            y += 4

    while (x <= 400 and case == 5):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)

        x += 2
        delay(0.01)
        if (x == 400):
            case += 1
            x -= 2

    while (case == 6):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+210*cos(rad/360*2*pi),300+210*sin(rad/360*2*pi))

        rad += 2
        delay(0.01)
        if (rad == 270):
            case = 1
            rad = -90

#delay(5)

close_canvas()
