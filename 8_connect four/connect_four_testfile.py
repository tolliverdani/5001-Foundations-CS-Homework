'''
    CS5001
    Spring 2020
    Project
    testfile.py

    Danielle Tolliver
    
'''
import os
from grid import *
from game import *

import unittest

empty_board =   []

full_board =    [['R', 'R', 'B', 'B', 'R', 'B', 'B'],
                 ['B', 'B', 'R', 'B', 'B', 'B', 'B'],
                 ['B', 'B', 'R', 'R', 'R', 'B', 'R'],
                 ['B', 'R', 'R', 'R', 'R', 'B', 'B'],
                 ['B', 'R', 'B', 'R', 'B', 'R', 'B'],
                 ['R', 'B', 'R', 'B', 'R', 'R', 'B']]

class TestConnectFour(unittest.TestCase):
    '''
    Class: TestConnectFour
    Attrbibutes: none
    '''
    def test_game_init(self):
        '''
        Method: test_game_init
        Parameters: none
        '''
        # checks attributes
        grid = Grid(1000, 1000)
        self.assertAlmostEqual(grid.width, 1000)
        self.assertAlmostEqual(grid.height, 1000)
        self.assertAlmostEqual(grid.rows, 6)
        self.assertAlmostEqual(grid.columns, 7)

        # tests an empty board and full board
        self.assertEqual(grid.board, empty_board)
        grid.board = full_board
        self.assertEqual(grid.board, full_board)

   
    def test_grid_init(self):
        '''
        Method: test_grid_init
        Parameters: none
        '''
        # checks attributes
        game = Game()
        self.assertEqual(game.scorefile, "score.txt")
        self.assertAlmostEqual(game.score, 0)
        self.assertAlmostEqual(game.turn, 0)

        # tests if the ints are out of range
        self.assertAlmostEqual(game.out_of_range(9), True)
        self.assertAlmostEqual(game.out_of_range(1), False)
        self.assertAlmostEqual(game.out_of_range(11), True)
        self.assertAlmostEqual(game.out_of_range(3), False)

        # tests reading the score for an empty file
        if os.path.exists('nofile.txt'):
            os.remove('nofile.txt')
        game.initialize_score('nofile.txt')
        self.assertEqual(game.score, 0)

        # tests reading the score in a test file
        with open('testscore.txt', 'w') as outfile:
            outfile.write('10')
        game.initialize_score('testscore.txt')
        self.assertEqual(game.score, 10)
        os.remove('testscore.txt')

        
def main():

    unittest.main(verbosity = 3)
    
main()
