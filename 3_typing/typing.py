'''
    CS5001
    Spring 2020
    Homework 3 - Problem 3
    typing.py

    Starter code: sentence.py

    Danielle Tolliver

    Results from the test:

    You typed 34 words in 21.69 seconds.
    Your wpm is 94.
    You made 0 mistakes, so your adjusted wpm is 94.
    
'''

import random
import time
import math

from sentence import *
from typing_functions import *

def main():

    #introduction to the game
    print("Ready to see how fast you type? ")
    begin = input("Type ENTER to begin. ")

    while not begin_program(begin):

        begin = input("You must type ENTER to begin. ")

    #starting stats for the user
    start_time = time.monotonic()
    user_sentence = ""
    total_errors = 0
    num_words = 0
    
    #starts program, calculates wpm and adjusted wpm, and prints results
    run_program(start_time, user_sentence, num_words, total_errors)

     
main()
