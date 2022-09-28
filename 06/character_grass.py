from pico2d import *
from math import *

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def run_circle():
    print("circle")

    cx, cy, r = 400,300,200
    for dig in range(-90,270,5):
        x = cx + r*cos(dig/180*pi)
        y = cy + r*sin(dig/180*pi)
        render_all(x,y)

def run_rectangle():
    print("rectangle")

#bottom line
    for x in range(50,750+1,10):
        render_all(x,90)

#right line
    for y in range(90,560+1,10):
        render_all(750,y)

#top line
    for x in range(750,50-1,-10):
        render_all(x,560)

#left line
    for y in range(560,90-1,-10):
        render_all(50,y)




while True:
    run_circle()
    run_rectangle()
    break



#grass.draw_now(400,30)
#character.draw_now(400,90)

#while (1):
#    x = 400
#    y = 90
#    case = 1
#    rad = -90
#    while (x <= 780 and case == 1):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(x,90)
#
#        x += 2
#        delay(0.01)
#        if (x == 780):
#            case += 1
#            x -= 2
#    
#    while (y <= 570 and case == 2):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(780,y)
#
#        y += 4
#        delay(0.01)
#        if (y == 570):
#            case += 1
#            y -= 4
#    
#    while (x >= 20 and case == 3):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(x,570)
#
#        x -= 2
#        delay(0.01)
#        if (x == 20):
#            case += 1
#            x += 2
#    
#    while (y >= 90 and case == 4):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(20,y)
#
#        y -= 4
#        delay(0.01)
#        if (y == 90):
#            case += 1
#            y += 4
#
#    while (x <= 400 and case == 5):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(x,90)
#
#        x += 2
#        delay(0.01)
#        if (x == 400):
#            case += 1
#            x -= 2
#
#    while (case == 6):
#        clear_canvas_now()
#        grass.draw_now(400,30)
#        character.draw_now(400+210*cos(rad/360*2*pi),300+210*sin(rad/360*2*pi))
#
#        rad += 2
#        delay(0.01)
#        if (rad == 270):
#            case = 1
#            rad = -90
#
##delay(5)
#
#close_canvas()
#