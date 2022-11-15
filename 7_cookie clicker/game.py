'''
    CS5001
    Spring 2020
    Homework 7
    game.py

    Danielle Tolliver
    
'''
import turtle
import os
from cookie import *

class Game:

    def __init__(self, scorefile, achievefile):

        self.scorefile = scorefile
        self.achievefile = achievefile

        # creating the cookie and initalizing stats
        self.cookie = Cookie()
        self.cookie.initialize_score(scorefile)
        self.cookie.initialize_achievements(achievefile)

        # creates a turtle for the stats
        self.user_stats = turtle.Turtle()
        

    def on_cookie(self, x, y):
        '''
        Parameters: self
        Function: checks if the click is within the cookie and then adds points,
        checks for bonus points and updates the header with the score... if the
        user clicks outside of the cookie, it saves the game and exits
        Returns: nothing
        '''
        # if the click is within the cookie range...
        if (-150 < x < 150) and (-150 < y < 150):
            self.cookie.add_point()
            self.cookie.bonus_points()
            self.str_user_stats()

        # else save the score and exit the game
        else:
            self.save_score()
            exit()

            
    def str_user_stats(self):
        '''
        Parameters: self
        Function: shows the user the updated score with each click
        Returns: nothing 
        '''
        # printing stats on top of screen
        self.user_stats.clear()
        self.user_stats.hideturtle()
        self.user_stats.penup()
        self.user_stats.setposition(0,300)
        self.user_stats.write("Your score is " + str(self.cookie.score),
                              font = (14), align = "center")


    def save_score(self):
        '''
        Parameters: self
        Function: saves the score when the user exits the game
        Returns: nothing
        '''        
        try:
            # writes the score in the file
            with open(self.scorefile, 'w') as outfile:
                self.cookie.score = str(self.cookie.score)
                outfile.write(self.cookie.score)

        # unless there's an error and then it lets you know
        except OSError or TypeError:
            print("Couldn't save your score, try again later.")
