'''
    CS5001
    Spring 2020
    Homework 3 - Problem 2
    nim_functions.py

    Danielle Tolliver
'''

import random


def is_over(number_beans):
    '''
    Name: is_over
    Inputs: number_beans
    Function: checks if the number of beans in the pile is > 3
    Outputs: True or False (boolean)
    '''
    if number_beans <= 1:
        return True        

    return False

def computers_turn(number_beans):
    '''
    Name: computers_turn
    Inputs: number_beans
    Function: computer selects random number between 1 - 3 for turn
    Outputs: turn (int)
    '''
    if number_beans == 3:
        turn = 2
    elif number_beans == 2:
        turn = 1
    else:
        turn = random.randint(1,3)
    
    return(turn)


def valid_turn(turn):
    '''
    Name: valid_turn
    Inputs: turn (int)
    Function: makes sure user only takes up to 3 beans
    Outputs: True or False (boolean)
    '''
    if turn == 1:
        return True
    elif turn == 2:
        return True
    elif turn == 3:
        return True
    return False


def users_turn():
    '''
    Name: users_turn
    Inputs: nothing
    Function: asks user how many beans to take; checks for valid answer
    Outputs: turn (int)
    '''
    turn = int(input("\nHow many beans do you want to take? "))
    while not valid_turn(turn):
        turn = int(input("You can only take up to 3 beans. Try again: "))

    return(turn)


def correct_guess(guess, outcome):
    '''
    Name: correct_guess
    Inputs: guess and outcome (both str)
    Function: correct_guess
    Outputs: 1 or 2 (int)
    '''  
    print("\nTossed a coin and got... ", outcome, ".\n", sep = "")

    if outcome == guess:
        print("You guessed right! You go first.")
        return(1)
    else:
        print("Better luck next time! I get to go first.")
        return(2)


def coin_flip():
    '''
    Name: coin_flip
    Inputs: nothing
    Function: randomly picks a number; even = heads, odd = tails
    Outputs: H or T (str)
    '''
    outcome = random.randint(1,2)
    
    if outcome % 2 == 0:
        return("H")
    
    else:
        return("T")


def valid_guess(guess_coin):
    '''
    Name: valid_guess
    Inputs: guess_coin (str)
    Function: goes inside the guess_coin function to determine if it's an
    acceptable answer, e.g. H or T
    Outputs: True or False (boolean)
    '''
    if guess_coin == "H":
        return True
    elif guess_coin == "T":
        return True

    return False


def guess_coin():
    '''
    Name: guess_coin
    Inputs: nothing
    Function: gets a guess from the user if the coin will be heads or tails
    Outputs: the guess from the user (str)
    '''    
    print("Lets toss a coin to determine who goes first.")
    guess_coin = input("Please guess heads (H) or tails (T): ")
    guess_coin = guess_coin.upper()

    while not valid_guess(guess_coin):
        guess_coin = input("Only heads (H) or tails (T) is valid. Try again: ")

    return(guess_coin)


def coin_toss():
    '''
    Name: coin_toss
    Inputs: nothing
    Function: runs functions within the function to see who goes first
    Outputs: 1 or 2 (int)
    '''    
    guess = guess_coin()
    outcome = coin_flip()

    return(correct_guess(guess, outcome))


