'''
    CS5001
    Spring 2020
    Homework 5 - Problem 1
    test_classify_functions.py

    Danielle Tolliver

'''

from classify_functions import *

test_list = ["apples", "apples", "banana", "orange", "grapefruit", "pear",
             "orange", "apples", "banana", "apples"]

test_sentence = ["hello there, I am a sentence and I am not very long."]


def test_count_frequency(test_list):
    '''
    Name: test_count_frequency
    Inputs: test_list (list)
    Function: takes the count_frequency function and tests it with test_list
    Outputs: nothing; just a print statement with expected and actual results
    '''
    no_duplicates = remove_duplicates(test_list)

    results = count_frequency(test_list, no_duplicates)
    print("Expected: 4, 2, 2, 1, 1\n",
          "Actual results: ", results, sep = "")
    

def test_remove_duplicates(test_list):
    '''
    Name: test_remove_duplicates
    Inputs: test_list
    Function: takes the remove_duplicates function and tests it with test_list
    Outputs: nothing; just a print statement with expected and actual results
    '''
    results = remove_duplicates(test_list)
    print("Expected: apples, banana, orange, grapefruit, pear\n",
          "Actual results: ", results, sep = "")
    
    
def main():

    no_duplicates = remove_duplicates(test_list)

    test_remove_duplicates(test_list)
    test_count_frequency(test_list)

main()
