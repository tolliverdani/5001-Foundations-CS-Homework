'''
    CS5001
    Spring 2020
    Homework 3 - Problem 2
    test_nim_functions.py

    Danielle Tolliver
'''

from nim_functions import *

def test_computers_turn(number_beans, expected):
    '''
    Name: test_computers_turn
    Inputs: number_beans (int) and outcome (int)
    Function: tests is the outcome of the computers turn is valid based on
    winning logic
    Outputs: Boolean indicating if the test passed
    '''
    actual = computers_turn(number_beans)
    print("\nTesting computer's turn... there are ", number_beans, " beans.",
          "\nExpected: ", expected, "\nActual: ", actual, sep = "")

def test_is_over(number_beans, expected):
    '''
    Name: test_is_over
    Inputs: number_beans (int)
    Function: tests if the game is over based on number of beans left
    Outputs: True or False (boolean)
    '''
    actual = is_over(number_beans)
    print("\nTesting is_over function... there are ", number_beans, " beans.",
          "\nExpected: ", expected, "\nActual: ", actual, sep = "")
    
def main():
    
    #test the random coin flip
    print(coin_flip())
    print(coin_flip())
    print(coin_flip())
    print(coin_flip())
    print(coin_flip())
    
    #test the guess against outcome
    correct_guess("T", "H")
    correct_guess("H", "T")
    correct_guess("H", "H")
    correct_guess("T", "T")
    
    #test the computer's turn
    test_computers_turn(3, 2)
    test_computers_turn(2, 1)

    #test the end of game signal
    test_is_over(3, False)
    test_is_over(2, False)
    test_is_over(1, True)
    
main()
