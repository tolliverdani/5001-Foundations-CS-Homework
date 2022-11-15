'''
    CS5001
    Spring 2020
    Homework 3 - Problem 1
    horizon.py

    Danielle Tolliver

'''

import turtle
from horizon_functions import *

SUN_Y_COORD = 100
SUN_X_COORD = 350
MOON_X_COORD = -500
RADIUS = 100

def main():

    #Setting up the scene and background
    screen = turtle.Screen()
    screen.bgcolor("light blue")
    screen.setup(width = 1000, height = 500)
    screen.tracer(0)
    draw_sun()

    #draws mooon, moves it forward and changes sky at the right coords
    draw_moon(screen)

main()
