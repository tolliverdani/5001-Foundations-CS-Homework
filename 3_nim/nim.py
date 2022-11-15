'''
    CS5001
    Spring 2020
    Homework 3 - Problem 2
    nim.py

    Danielle Tolliver
'''

import random
from nim_functions import *


def main():

    number_beans = random.randint(5,30)

    #introduction to the game
    name = input("To start off, please tell me your name: ")
    print("\nNice to meet you, ", name, ". Let's get this started!\n"
          "We are starting with... ", number_beans, " beans.\n", sep = "")

    #runs the coin toss function to see who goes first
    player = coin_toss()

    #runs the game until there is only one bean
    while not is_over(number_beans):

        if player == 1:
            turn = int(users_turn())
            number_beans -= turn
            print("You took ", turn, " bean(s). There are ",
                  number_beans, " beans left.", sep = "")
            player = 2

        elif player == 2:
            turn = int(computers_turn(number_beans))
            number_beans -= turn
            print("\nI am taking ", turn, " bean(s). There are ",
                  number_beans, " beans left.", sep = "")
            player = 1

    #determines the winner and prints a statement
    if player == 2:
        print("\nGame over!! You beat me!")

    elif player == 1:
        print("\nGame over!! I beat you!")

    
main()
