'''
    CS5001
    Spring 2020
    Homework 3 - Problem 3
    typing_functions.py

    Danielle Tolliver
'''

import random
import time
import math

from sentence import *
from typing_functions import *


def calculate_wpm(num_words, time):
    '''
    Name: calculate_wpm
    Inputs: num_words (float) and time (float)
    Function: calculates the words per minute 
    Outputs: words_per_minute (float)
    '''
    minutes = 60 / round(time, 2)
    words_per_minute = float(math.floor(minutes * num_words))
    return(words_per_minute)

  
def calculate_adjusted(num_words, num_mistakes, time):
    '''
    Name: calculate_adjusted
    Inputs: num_words (float), num_mistakes (float) and time (float)
    Function: calculates the words per minute (adjusted for errors)
    Outputs: adjusted_words_per_minute
    '''
    minutes = 60 / round(time, 2)

    if num_words - num_mistakes <= 0:
        adjusted_words = 0
    else:
        adjusted_words = num_words - num_mistakes

    adjusted_words_per_minute = float(math.floor(minutes * adjusted_words))
    return(adjusted_words_per_minute)    
  

def run_program(start_time, user_sentence, num_words, total_errors):
    '''
    Name: run_program
    Inputs: user_sentence (str), num_words (int), total_errors (int)
    Function: produces random sentences for the test,  records words and errors,
    calls calculate_wpm and calculate_adjusted functions to store results
    Outputs: nothing; prints results to user
    '''
    while not end_program(user_sentence):

        sentence = ("\n" + select_sentence())
        print(sentence)
        user_sentence = input()

        num_words += int(count_words(sentence))
        total_errors += count_mismatches(sentence, user_sentence)

    total_errors -= float(count_words(sentence))
    total_errors = math.floor(total_errors) - 1

    #when the program is finished, calculate new stats
    end_time = time.monotonic()
    duration = round(float(end_time - start_time),2)
    
    print("\nYou typed ", num_words, " words in ", duration, " seconds.",
          "\nYour wpm is ", int(calculate_wpm(num_words, duration)), ".",
          "\nYou made ", total_errors, " mistakes, so your adjusted wpm is ",
          int(calculate_adjusted(num_words, total_errors, duration)), ".",
          sep = "")
    return(num_words)


def end_program(user_sentence):
    '''
    Name: end_program
    Inputs: user_sentence (str)
    Function: checks to see if the user has typed DONE
    Outputs: returns True if true (boolean)
    '''
    if user_sentence == "DONE":
        return True


def begin_program(begin):
    '''
    Name: begin_program
    Inputs: begin (str)
    Function: checks to see if the user has typed ENTER (in any capitalization)
    Outputs: returns True if true (boolean)
    '''
    begin = begin.upper()
    
    if begin == "ENTER":
        return True
