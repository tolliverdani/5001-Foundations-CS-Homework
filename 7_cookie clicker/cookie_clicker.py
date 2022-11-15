'''
    CS5001
    Spring 2020
    Homework 7
    cookie_clicker.py

    Danielle Tolliver

'''

import turtle

SCORE_FILE = "score.txt"
ACHIEVEMENTS = "achievements.txt"

from game import Game
from cookie import Cookie

def main():
    
    # creating the game
    game = Game(SCORE_FILE, ACHIEVEMENTS)

    # creating the screen
    screen = turtle.Screen()
    screen.setup(width = 1000, height = 750)
    screen.bgpic('cookie.gif')

    # showing first user stats
    game.str_user_stats()

    # listening for clicks
    turtle.onscreenclick(game.on_cookie)
            
main()
