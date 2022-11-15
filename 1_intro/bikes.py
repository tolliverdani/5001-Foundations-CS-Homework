'''
    CS5001
    Spring 2020
    Homework: bikes.py
    Danielle Tolliver

    Suppose you are a bike shop owner who puts together bikes from spare parts.
    Your customers come to you with parts they’ve (legitimately) found in their
    garages,from scrap metal heaps, etc., and they ask you to build them all the
    bikes you can make with the parts they give you. You build the bikes, charge
    them a big pile of money for the privilege, and keep the leftover parts for
    yourself.

    It takes the following parts to create one bicycle:
        2 wheels
        1 frame
        50 links (to make a chain)

    Write a Python program to calculate how many bikes you can make from the parts
    the user gives you. You may assume they always give you “good” input, i.e., all
    whole numbers, and no negatives. Your output can print simply “bikes” or “bike(s)”
    each time -- don’t worry about singular/plural.

    Test case #1:
    Wheels: 6
    Frames: 6
    Links: 250
    Bikes: 3
    Leftovers: 0 wheels, 3 frames, 100 links

    Test case #2:
    Wheels: 2
    Frames: 5
    Links: 600
    Bikes: 1
    Leftovers: 0 wheels, 4 frames, 550 links

    Test case #3:
    Wheels: 1
    Frames: 2
    Links: 50
    Bikes: 0
    Leftovers: 1 wheels, 2 frames, 50 links
'''

import math


def main():
    # Get inputs from user and store as int variables
    wheels = int(input("How many wheels do you have?\n"))
    frames = int(input("How many frames do you have?\n"))
    links = int(input("How many links do you have?\n"))

    # Use the min() function to figure out the number of bikes
    total_bikes = math.floor(min(wheels / 2, frames / 1, links / 50))

    # Calculate leftover parts
    leftover_wheels = wheels - (2 * total_bikes)
    leftover_frames = frames - (1 * total_bikes)
    leftover_links = links - (50 * total_bikes)

    # Print the values for the user
    print("\nAll totaled up, you've got", total_bikes, "bike(s) coming.",
          "I'm keeping the leftovers for myself.\nLeftovers:",
          leftover_wheels, "wheels,", leftover_frames, "frames, and",
          leftover_links, "links.")


main()
