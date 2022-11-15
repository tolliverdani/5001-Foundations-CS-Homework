'''
    CS5001
    Spring 2020
    Project
    grid.py

    Danielle Tolliver

'''

import turtle
import math

from game import *

ROWS = 6
COLUMNS = 7

class Grid:
    ''' class: Grid
        Attributes: width, height, rows, columns, grid_matrix
        Methods: make_board, draw_board, draw_column, update_board, is_full
    '''
    
    def __init__(self, width, height):
        '''
        Constructor: creates an new instance of game
        Parameters: width (int), height (int)
        '''
        self.width = width
        self.height = height
        self.rows = ROWS
        self.columns = COLUMNS
        self.board = []
            
    def make_board(self):
        '''
        Method: make_board
        Parameters: none
        '''
        # for all the columns, make an empty list
        for i in range(self.columns):
            self.temp_list = []

            # for each row, put a "O" for empty
            for j in range(self.rows):
                self.temp_list.append("O")

            # add each full column to the main board list
            self.board.append(self.temp_list)

        # once finished, draw the board
        self.draw_board()

    
    def draw_board(self):
        '''
        Method: draw_board
        Parameters: none
        '''
        # for each column in the range of board, draw the column
        for col in range(len(self.board)):

            self.draw_column(col)
    
    
    def draw_column(self, col):
        '''
        Method: draw_column
        Parameters: col (int)
        '''
        # for each row in the column...
        for i in range(len(self.board[col])):

            # create turtle and change coordinates according to the row value
            self.col_coord = (self.width / 2) * -1 + (100 * col) + 100 
            self.row_coord = (self.height / 2) - (100 * i) - 200
            self.new_dot = turtle.Turtle()
            self.new_dot.speed(10)
            self.new_dot.penup()
            self.new_dot.goto(self.col_coord, self.row_coord)

            # depending on player value, add shape to the board
            if self.board[col][i] == "O":
                self.new_dot.shape("empty.gif")
                
            elif self.board[col][i] == "R":
                self.new_dot.shape("red_1.gif")

            elif self.board[col][i] == "B":
                self.new_dot.shape("blue_1.gif")


    def update_board(self, selection, color):
        '''
        Method: update_board
        Parameters: selection (int), color (str)
        '''
        self.color = color
        self.selection = selection

        # for each row in the column, iterate backwards from the bottom
        for i in range(len(self.board[selection])-1, -1, -1):

            # if it's empty add player's letter, otherwise continue through the list
            if self.board[selection][i] == "O":
                self.board[selection][i] = self.color
                break

        # then draw the column for the user
        self.draw_column(self.selection)


    def is_full(self):
        '''
        Method: is_full
        Parameters: none
        '''
        count = 0

        # cound all of the "O"s in the board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "O":
                    count += 1

        return count
        
