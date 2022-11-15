'''
    CS5001
    Spring 2020
    Homework 7
    cookie_clicker.py

    Danielle Tolliver

'''
import sys
import turtle

from game import *
from grid import *

SCOREFILE = "score.txt"


def main():

    # create the game
    game = Game()
    score = game.initialize_score(SCOREFILE)

    # take turns while the game isn't over
    game.player_turn()

    print("Game over!")
    
    #saves score at the end of game
    score += 1
    game.save_score(SCOREFILE)

    
main()

