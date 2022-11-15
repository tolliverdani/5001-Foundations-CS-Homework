'''
    CS5001
    Spring 2020
    Homework 3 - Problem 1
    horizon_functions.py

    Danielle Tolliver

'''

import turtle 

SUN_Y_COORD = 100
SUN_X_COORD = 300
MOON_X_COORD = -500
RADIUS = 100


def change_sky(coord, screen):
    '''
    Name: change_sky
    Inputs: coordinates (int), and screen
    Function: tracks the coordinates and changes the backgound of the sky
    when the moon crosses the sun
    Outputs: nothing
    '''
    if ((SUN_X_COORD + RADIUS) > coord > (SUN_X_COORD - RADIUS)):

        screen.bgcolor("dark grey")

    else:

        screen.bgcolor("light blue")


def move_moon(moon, screen):
    '''
    Name: move_moon
    Inputs: moon and screen
    Function: moves turtle forward 1px and clears/redraws for animation
    Outputs: nothing
    '''
    coord = MOON_X_COORD

    while True:

            change_sky(coord, screen)
            moon.clear()
            moon.dot(RADIUS, "grey")
            screen.update()
            moon.forward(1)
            coord += 1

            if coord == 450:
                return False
                

def draw_moon(screen):
    '''
    Name: drwa_moon
    Inputs: screen
    Function: draws the moon with the dot function
    Outputs: nothing
    '''
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.penup()
    moon.goto(MOON_X_COORD, SUN_Y_COORD)
    moon.dot(RADIUS, "grey")

    move_moon(moon, screen)


def draw_sun():
    '''
    Name: draw_sun
    Inputs: nothing
    Function: draws the sun with the dot function
    Outputs: nothing
    '''
    sun = turtle.Turtle()
    sun.hideturtle()
    sun.penup()
    sun.goto(SUN_X_COORD, SUN_Y_COORD)
    sun.dot(RADIUS, "yellow")

