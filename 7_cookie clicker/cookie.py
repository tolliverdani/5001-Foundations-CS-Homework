'''
    CS5001
    Spring 2020
    Homework 7
    cookie.py

    Danielle Tolliver

'''

import turtle
from game import *

class Cookie:

    def __init__(self):

        self.score = 0
        self.achievements = {}

    def add_point(self):
        '''
        Parameters: self
        Function: adds a point to the score
        Returns: self.score (int)
        '''
        # adds a point to the score
        self.score += 1

    def initialize_score(self, scorefile):
        '''
        Parameters: self, scorefile (.txt)
        Function: reads the scorefile and updates the value in the game
        Returns: self.score (int)
        '''
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

    def initialize_achievements(self, achievement_file):
        '''
        Parameters: self, schievement_file (.txt)
        Function: reads the achievements file, splits lines, and creates
        dictionary from the last 2 items per line 
        Returns: a dictionary
        '''
        try:
            # opens the file and checks for score
            with open(achievement_file, 'r') as infile:

                temp_list = infile.readlines()

                # for each line, split the contents and save the last 2 in dict
                for i in range(len(temp_list)):
                    split_temp_list = temp_list[i].split()
                    self.achievements[
                        int(split_temp_list[1])] =int(split_temp_list[2])
        # unless theres no file                    
        except OSError:
            return
   
    def bonus_points(self):
        '''
        Parameters: self
        Function: looks at the score and checks it against the achievements
        dictionary; if score is in dictionary, it adds the points to score
        and tells the user they are awesome
        Returns: self.score (int)
        '''
        # if the score reaching a place in achievements it lets user know
        if self.score in self.achievements:
            print("Awesome job!! You just got ", self.achievements[self.score],
                  " bonus point[s].", sep = "")
            # and adds the bonus to their score
            self.score += self.achievements[self.score]
