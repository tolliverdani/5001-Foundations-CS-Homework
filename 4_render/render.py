'''
    CS5001
    Spring 2020
    Homework 4 - Problem 3
    render.py

    Danielle Tolliver
 
    --
    
    Learned how to remove [] and '' using this link:
    https://stackoverflow.com/questions/3900054/python-strip
    -multiple-characters
    
'''
import turtle
import math

P = "purple"
B = "black"
L = "light blue"
Y = "yellow"
O = "brown"
R = "red"

SCREEN_SIZE = 500

from render_lists import *

def draw_pixel_by_pixel(pixel, color):
    '''
    Name: draw_pixel
    Inputs: color
    Function: draws one pixel at a time
    Outputs: nothing
    '''

    pixel.forward(10)
    pixel.left(90)
    pixel.forward(10)
    pixel.left(90)
    pixel.forward(10)
    pixel.left(90)
    pixel.forward(10)
    pixel.left(90)
    pixel.forward(10)
    
def main():

    #Setting up the scene and background
    screen = turtle.Screen()
    screen.setup(width = SCREEN_SIZE, height = SCREEN_SIZE)

    pixel = turtle.Turtle()
    
    for i in range (3):

        draw_pixel_by_pixel(pixel, L)

main()
