'''
    CS5001
    Spring 2020
    Homework 5 - Problem 1
    classify_functions.py

    Danielle Tolliver

'''


from classify_data import *

import random


def compare_training_and_frequency(frequency, no_duplicates):
    '''
    Inputs: frequency (list), no_duplicates (list)
    Function: adds words from no_duplicates that are frequently used to new list
    Outputs: frequently_used_words (with no duplicates) (list)
    ''' 
    highest_frequency = find_max(frequency)
    frequently_used_words = []

    # uses frequency location to extrapolate words with high frequency
    for i in range(len(highest_frequency)):
        for j in range(len(frequency)):
            if highest_frequency[i] == frequency[j]:  
                frequently_used_words.append(no_duplicates[j])

    # then before it returns the result, it removes the extra duplicates        
    return(remove_duplicates(frequently_used_words))


def find_max(frequency):
    '''
    Inputs: frequency (list)
    Function: takes the frequency list and sorts it in descending order;
    finds the top 5 counts and adds those to a shorter list: highest_frequency
    Outputs: highest_frequency (list)
    '''             
    frequency_sort = frequency.copy()
    frequency_sort.sort(reverse = True)
    highest_frequency = []

    # only takes the words with more than one occurence
    for i in range(0, 5):
        if frequency_sort[i] > 1:
            highest_frequency.append(frequency_sort[i])
        
    return(highest_frequency)


def count_frequency(training_list, no_duplicates):
    '''
    Inputs: training_list (list), no_duplicates (list)
    Function: takes training_list and counts frequently of words
    Outputs: a list with the frequency of words (list)
    ''' 
    frequency = []

    # counts and adds to a new list (note: order matches training_list)
    for words in no_duplicates:
        frequency.append(training_list.count(words))

    return(frequency)


def remove_duplicates(clean_words):
    '''
    Inputs: clean_words
    Function: the list of clean words removes any duplicates
    Outputs: a list unique words (list)
    '''            
    no_duplicates = []

    # makes a list with no repeated words
    for words in clean_words:
        if words not in no_duplicates:
            no_duplicates.append(words)

    return(no_duplicates)
    

def sentence_to_words(training_data, ignore_words):
    '''
    Inputs: training_data (list), ignore_words (list)
    Function: takes the training list and removes all of the ignore_words
    Outputs: a list without ignore_words (list)
    --
    Learned how to convert sentences in list to words in list here:
    https://stackoverflow.com/questions/29068413/splitting-a-list-
    of-sentences-into-separate-words-in-a-list
    
    '''
    # turns the list of strings into a list of words
    training_list = " ".join(training_data).split(" ")
    clean_words = []

    # makes all words lower case and removes any stopwords
    for words in training_list:
        words = words.lower()
        if words not in ignore_words:
            clean_words.append(words)

    return(clean_words)


def gina_training_set():
    '''
    Inputs: nothing
    Function: takes Gina's list and finds the top frequently used words
    Outputs: a list of frequently used words (list)
    ''' 
    gina_words = []

    # singles out gina's most frequently used words
    clean_words = sentence_to_words(GINA, STOPWORDS)
    no_duplicates = remove_duplicates(clean_words)
    frequency = count_frequency(clean_words, no_duplicates)
    gina_words = (compare_training_and_frequency(frequency, no_duplicates))

    return(gina_words)


def holt_training_set():
    '''
    Inputs: nothing
    Function: takes Holt's list and finds the top frequently used words
    Outputs: a list of frequently used words (list)
    ''' 
    holt_words = []

    # singles out holt's most frequently used words
    clean_words = sentence_to_words(HOLT, STOPWORDS)
    no_duplicates = remove_duplicates(clean_words)
    frequency = count_frequency(clean_words, no_duplicates)
    holt_words = (compare_training_and_frequency(frequency, no_duplicates))

    return(holt_words)


def rosa_training_set():
    '''
    Inputs: nothing
    Function: takes Rosa's list and finds the top frequently used words
    Outputs: a list of frequently used words (list)
    ''' 
    rosa_words = []

    # singles out rosa's most frequently used words
    clean_words = sentence_to_words(ROSA, STOPWORDS)
    no_duplicates = remove_duplicates(clean_words)
    frequency = count_frequency(clean_words, no_duplicates)
    rosa_words = (compare_training_and_frequency(frequency, no_duplicates))

    return(rosa_words)


def jake_training_set():
    '''
    Inputs: nothing
    Function: takes Jake's list and finds the top frequently used words
    Outputs: a list of frequently used words (list)
    ''' 
    jake_words = []

    # singles out jake's most frequently used words
    clean_words = sentence_to_words(JAKE, STOPWORDS)
    no_duplicates = remove_duplicates(clean_words)
    frequency = count_frequency(clean_words, no_duplicates)
    jake_words = (compare_training_and_frequency(frequency, no_duplicates))

    return(jake_words)


def choice_two(user_input):
    '''
    Inputs: user_input
    Function: lets user write a sentence and checks for likely said character,
    returns results in a print statement; if no result, then inconclusive
    Outputs: nothing; just a print statement and goes to user_menu again
    '''    
    # below creates the training set for each character and sets their score to 0
    jake_words = jake_training_set()
    jake_score = 0
    
    rosa_words = rosa_training_set()
    rosa_score = 0
    
    holt_words = holt_training_set()
    holt_score = 0
    
    gina_words = gina_training_set()
    gina_score = 0

    #checks if the words are frequently used by jake and gives a score
    for i in range(len(jake_words)):
        if jake_words[i] in user_input:
            jake_score += 1

    #checks if the words are frequently used by rosa and gives a score
    for i in range(len(rosa_words)):
        if rosa_words[i] in user_input:
            rosa_score += 1

    #checks if the words are frequently used by holt and gives a score
    for i in range(len(holt_words)):
        if holt_words[i] in user_input:
            holt_score += 1

    #checks if the words are frequently used by gina and gives a score
    for i in range(len(gina_words)):
        if gina_words[i] in user_input:
            gina_score += 1

    # finds the max score between all the characters
    max_score = max(jake_score, rosa_score, holt_score, gina_score)

    # returns the output to the user
    if max_score == jake_score:
        print("This was likely said by... Jake!\n")
    elif max_score == rosa_score:
        print("This was likely said by... Rosa!\n")
    elif max_score == holt_score:
        print("This was likely said by... Holt!\n")
    elif max_score == gina_score:
        print("This was likely said by... Gina!\n")
    else:
        print("Results are inconclusive.\n")

    # then goes back to the user menu
    user_menu()


def choice_one():
    '''
    Inputs: nothing
    Function: picks random sentence, checks for exact match against characters,
    returns results in a print statement; if no result, runs choice_two to find
    likely character
    Outputs: nothing; just a print statement and goes to user_menu again
    '''
    # computer picks a random sentence
    phrase_one = random.choice(TESTING)
    print("The random phrase is... ", phrase_one)

    match = 0

    # checks if the random sentence matches any of jake's
    for sentence in JAKE:
        if phrase_one == sentence:
            match = 1
            print("This was said by... Jake!\n")

    # checks if the random sentence matches any of roas's
    for sentence in ROSA:
        if phrase_one == sentence:
            match = 1
            print("This was said by... Rosa!\n")

    # checks if the random sentence matches any of holt's      
    for sentence in HOLT:
        if phrase_one == sentence:
            match = 1
            print("This was said by... Hult!\n")

    # checks if the random sentence matches any of gina's
    for sentence in GINA:
        if phrase_one == sentence:
            match = 1
            print("This was said by... Gina!\n")

    # if no match, give option to check against the database or return to menu
    if match == 0:

        print("\nThere was no clear match. Would you like to check character ",
              "against our database?\n",
              "\t1 -- Yes\n",
              "\t2 -- No, return to menu\n",
              "\t3 -- Quit\n", sep = "")
        
        choice = int(input("Selection: "))

        # ensure the user puts in a valid choice
        while not valid_choice(choice):
            choice = int(input("Invalid selection. Try again."))
            
        if choice == 1:
            choice_two(phrase_one)

    # return to menu        
    user_menu()          

    
def valid_choice(choice):
    '''
    Inputs: choice (int)
    Function: ensures the choice is one of the menu options
    Outputs: True or False (boolean)
    '''
    # checks to make sure the choice is a valid answer
    if choice == 1:
        return True
    elif choice == 2:
        return True
    elif choice == 3:
        return True
    return False


def user_menu():
    '''
    Inputs: nothing
    Function: provides a menu for the user when the program starts
    Outputs: nothing
    '''
    # bring up the menu for the user and present choices
    print("Hello, welcome to 'Who Said?' with Brooklyn 99.\n")
    print("Please select from the following menu:\n\n",
          "\t1 -- Choose a test quote at random\n",
          "\t2 -- Type a quote in yourself\n",
          "\t3 -- Quit")

    # ensure choice is valid      
    choice = int(input("\nEnter your choice now!\n"))
    while not valid_choice(choice):
        choice = int(input("\nInvalid choice, try again:\n"))

    # goes to menu options
    if choice == 1:
        choice_one()
    elif choice == 2:
        user_input = input("Enter a quote here:\n")
        choice_two(user_input)
    elif choice == 3:
        exit()
