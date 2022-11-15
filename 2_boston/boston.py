'''
    CS5001
    Spring 2020
    Homework: boston.py, boston_driver.py, test_boston.py
    Danielle Tolliver

'''

import turtle
from boston_driver import *

def main():

    #Set up the background and WVH
    screen = turtle.Screen()
    screen.setup(width = 800, height = 565)
    screen.bgpic("boston_map_new.png")
    draw_circle("red", 5)
    write_at_location("West Village H","")

    #Interact with the user to get info
    name = input("Where would you like to go? ")
    new_lat = float(input("What is the latitude? "))
    new_long = float(input("What is the longitude? "))

    #Move the turtle to new location and draw a circle
    move_turtle(new_lat, new_long)
    draw_circle("blue", 5)
    
    #Interact with the user again with name and distance
    distance = calc_distance(new_lat, new_long)
    print("\n", name, " is ", distance, " miles from West Village H.",
          "\nBetter start walking!", sep = "")
    
    
    write_at_location(name, distance)
    
main()
