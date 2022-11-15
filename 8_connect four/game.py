'''
    CS5001
    Spring 2020
    Project
    game.py

    Danielle Tolliver

'''

WIDTH = 800
HEIGHT = 800
SCOREFILE = "score.txt"
EMPTY = "empty.gif"
RED = "red_1.gif"
BLUE = "blue_1.gif"

import turtle
import math
import random

from grid import *

class Game:
    '''
    class: Game
    Attributes: grid, screen, width, height, scorefile, score, turn
    Methods: set_up_screen, find_column, player_turn, out_of_range, str_user_stats
    initialize_score, save_score
    '''
    def __init__(self):
        '''
        Constructor: creates a new instance of game
        Parameters: none
        '''
        self.width = WIDTH
        self.height = HEIGHT
        self.scorefile = SCOREFILE
        self.score = 0
        self.turn = 0
        
        # sets up the screen and registers all the shapes
        self.screen = turtle.Screen()
        self.screen.setup(width = WIDTH, height = HEIGHT)
        self.screen.register_shape(EMPTY)
        self.screen.register_shape(RED)
        self.screen.register_shape(BLUE)

        # running methods to launch the game
        self.user_stats = turtle.Turtle()
        self.clicker = turtle.Turtle()

         
    def player_turn(self):
        '''
        Method: player_turn
        Parameters: none
        '''
        # makes the grid for the game to begin
        self.grid = Grid(self.width, self.height)
        self.grid.make_board()
        
        # plays the game while True...
        while True:

            #unless the grid is full and it calls Game Over!
            if self.grid.is_full() == 0:
                print("Tie - game over!")
                return False

            # starts on human player and prompts for column to drop piece
            elif self.turn % 2 == 0:

                # assigns the human player "your" to update prompt on the screen
                self.player = "your"
                self.str_user_stats(self.player)
                self.color = "R"

                # asks player for int until it's valid
                self.selection = int(input("Pick your column: "))
                while self.out_of_range(self.selection):
                    self.selection = int(input("Please try again. " +
                                               "Pick your column: "))

                # takes the valid selection and updates the board
                self.grid.update_board(self.selection, self.color)

            # once it is the computer's turn... 
            elif self.turn % 2 == 1:

                # computer is assigned "my" to update prompt on the screen
                self.player = "my"
                self.str_user_stats(self.player)
                self.color = "B"

                # computer randomly picks an int from 0 - 6 until it's valid
                self.selection = random.randint(0,6)
                print("I have chosen column: ", self.selection)
                
                try:
                    self.grid.update_board(self.selection, self.color)
                    
                except:
                    self.selection = random.randint(0,6)
            
            self.turn += 1
            

    def out_of_range(self, selection):
        '''
        Method: out_of_range
        Parameters: selection (int)
        '''
        self.selection = selection

        # if the selection is not within 0 - 6 return False
        if 0 <= self.selection <= 6:
            return False
        else:
            return True

                    
    def str_user_stats(self, player):
        '''
        Method: str_user_stats
        Parameters: player (str)
        '''
        self.player = player
        
        # creates a turtle to print stats on top of screen during gameplay
        self.user_stats.clear()
        self.user_stats.hideturtle()
        self.user_stats.penup()
        self.user_stats.setposition(0,300)

        # chooses text color based on who the player is
        if player == "my":
            self.user_stats.color("blue")
        else:
            self.user_stats.color("red")

        # update the text on the game to show score and who's playing
        self.user_stats.write("Current score: " + str(self.score) + ". It is "
                              + self.player + " turn", font = (60),
                              align = "center")


    def initialize_score(self, scorefile):
        '''
        Method: initialize_score
        Parameters: scorefile
        '''
        self.scorefile = scorefile
        
        try:
            # opens the file and checks for score
            with open(scorefile, 'r') as infile:
                self.score = infile.read()

                try:
                    # if it can, make it an int
                    self.score = int(self.score)

                # but if not, make it 0        
                except ValueError:
                    self.score = 0

        # if nothing, assume 0 points
        except OSError:
            self.score = 0


    def save_score(self, scorefile):
        '''
        Method: save_score
        Parameters: none
        '''
        self.scorefile = scorefile
        
        try:
            # writes the score in the file
            with open(self.scorefile, 'w') as outfile:
                self.score = str(self.score)
                outfile.write(self.score)

        # unless there's an error and then it lets you know
        except OSError or TypeError:
            print("Couldn't save your score, try again later.")


    def find_column(self, x, y):
        '''
        Method: find_column
        Parameters: x, y
        Note: I got this function to work, but it can't be used in the game because
        it's infinite looping... I couldn't figure it out before submission.
        '''
        self.x_coord = x

        # selects the column based on the x coordinate of the click
        if -350 < self.x_coord < -250:
            self.selection = 0
        elif -250 < self.x_coord < -150:
            self.selection = 1
        elif -150 < self.x_coord < -50:
            self.selection = 2
        elif -50 < self.x_coord < 50:
            self.selection = 3
        elif 50 < self.x_coord < 150:
            self.selection = 4
        elif 150 < self.x_coord < 250:
            self.selection = 5
        elif 250 < self.x_coord < 350:
            self.selection = 6

        # in another version, I had this method run after the selection was made...
        self.grid.update_board(self.selection, self.color)
