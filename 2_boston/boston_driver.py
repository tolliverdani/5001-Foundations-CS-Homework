'''
    CS5001
    Spring 2020
    Homework: boston.py, boston_driver.py, test_boston.py
    Danielle Tolliver

    --
    
    Simplified drawing a circle with help from this website:
    https://www.tutorialsandyou.com/python/how-to-draw-color-filled-
    shapes-in-python-turtle-17.html

'''

import turtle
import math

WVH_LAT = 42.338574
WVH_LONG = -71.0945489

def draw_circle(color, radius):
    '''
    Inputs: radius for the circle
    Function: draws a circle with the turtle in variable color and radius
    Returns: nothing; should see a circle on the program screen
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def move_turtle(lat, long):
    '''
    Inputs: x and y from a function below
    Function: moves the turtle to the new location
    Returns: nothing; but you should see the turtle move
    '''
    x = calc_x(lat, long)
    y = calc_y(lat, long)

    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)


def calc_x(lat, long):
    '''
    Inputs: lat and long of new location
    Function: finds the new x coord. of the location
    Returns: the x coord. for the new location (float)
    '''
    x_dist = (long - WVH_LONG) * 4000000 * math.cos((lat + WVH_LAT)
                                                    * 3.14 / 360) / 360
    x = int(x_dist)

    return(x)


def calc_y(lat, long):
    '''
    Inputs: lat and long of new location
    Function: finds the new y coord. of the location
    Returns: the y coord. for the new location (float)
    '''    
    y_dist = (lat - WVH_LAT) * 4000000 / 360
    y = int(y_dist)
    
    return(y)

    
def calc_distance(lat, long):
    '''
    Inputs: lat and long of the new location
    Function: finds distance between WVH and new location
    Returns: the distance (float)
    ''' 
    distance = (110.25 * math.sqrt(((lat - WVH_LAT)
                                    ** 2) + (((long - WVH_LONG)
                                              * math.cos(WVH_LAT))
                                                             ** 2)))
    distance = round(distance,2)

    return(distance)


def write_at_location(name, distance):
    '''
    Inputs: name (string) and distance (int)
    Function: writes some text next to the new location
    Returns: nothing; should see the text next to the new location
    '''
    words = (str(name)+"\n"+str(distance))
    turtle.write(words)

