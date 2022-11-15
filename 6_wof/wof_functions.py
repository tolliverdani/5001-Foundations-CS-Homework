'''
    CS5001
    Spring 2020
    wof_driver.py

    Danielle Tolliver
'''

from random import *

    
'''

def update_file(filename, score):
    '' Function: update_file
        Parameters: filename (string), score (int)
        Returns: nothing
    ''
    try:
        with open(filename, 'w') as outfile:
            outfile.write(score)
    except OSError:
        print("Could save your score, try again later.")
'''


def show_letters(phrase, guessed_letters):
    '''
    Name: show_letters
    Inputs: phrase (string), hidden_letters (list)
    Function: checks each letter in phrase against the list of guesses
    and compiles the string to include each guess
    Outputs: display_phrase (string)
    '''
    display_phrase = ""

    # for each character in the phrase
    for char in phrase:

        # so it only looks at alphabetic characters 
        if (ord(char) >= 97 and ord(char) <= 122):

            # if the character is in the guessed_letters list, shows it
            if char in guessed_letters:
                display_phrase += char
            # else it leaves the letter as an underscore to hide it
            else:
                display_phrase += "_ "

        # if it's not an alphabetic character, it keeps it unchanged phrase
        else:
            display_phrase += char

    # returns the display phrase
    return(display_phrase)           


def guess_letter(phrase):
    '''
    Name: guess_letter
    Inputs: phrase (string)
    Function: runs through each guess and prints current status
    Outputs: nothing
    '''
    guessed_letters = []

    print(show_letters(phrase, hidden_letters))
    # for the 5 turns... 
    for i in range(5):

        # user guesses a letter and we convert it to lowercase
        guess = input("\nGuess a letter: ")
        guess = guess.lower()

        # if the letter is in the phrase, adds to list guessed_letters
        if guess in phrase:
            guessed_letters.append(guess)

        # rewrites the phrase each turn so it can show the guessed_letters  
        display_phrase = show_letters(phrase, guessed_letters)
        print(display_phrase)


def find_phrase(data_file):
    '''
    Name: find_phrase
    Inputs: nothing
    Function: picks random line from wof.txt and shows hint to player
    Outputs: phrase to guess (string)
    '''
    # creating an empty list to put the phrase and hint in
    puzzle = []

    # picks random number and finds puzzle corresponding to location
    random_num = randint(0,(len(data_file)))
    puzzle = data_file[random_num].split(":")

    # saves the puzzle as a phrase and makes it lowercase
    phrase = puzzle[1]
    phrase = phrase.lower()

    # tells user the hint associated with the puzzle
    print("\nHere is your hint:", puzzle[0], "\n")

    return(phrase)


def clean_data():
    '''
    Name: clean_data
    Inputs: nothing
    Function: cleans up the data in wof.txt
    Outputs: list with category and hint
    '''    
    try:
        # read the data file
        with open("wof.txt", "r") as infile:
            
            # dump all data into data_file
            data_file = infile.read().splitlines()
            return(data_file)

    # if there is an error it'll let the user know    
    except OSError:
        print('Couldn\'t load anything from datafile')    


def valid_choice(choice):
    '''
    Name: valid_choice
    Inputs: choice (char)
    Function: ensures the choice is one of the menu options
    Outputs: True or False (boolean)
    '''
    # checks to make sure the choice is a valid answer
    if choice == "g":
        return True
    elif choice == "s":
        return True
    elif choice == "q":
        return True
    return False


def user_menu():
    '''
    Name: user_menu
    Inputs: nothing
    Function: runs the user menu for player to select from
    Outputs: nothing, but runs the corresponding choice's function
    '''
    data_file = clean_data()
    phrase = find_phrase(data_file)
    
    # bring up the menu for the user and present choices
    print("Please select from the following menu to begin:\n\n",
          "\tG -- Guess a letter\n",
          "\tS -- Solve\n",
          "\tQ -- Quit")

    # ensure choice is valid      
    choice = input("\nEnter your choice now! ")
    choice = choice.lower()
    while not valid_choice(choice):
        choice = input("\nInvalid choice, try again:\n")

    # goes to menu options
    if choice == "g":
        guess_letter(phrase)
    elif choice == "s":
        solve_answer(phrase)
    elif choice == "q":
        exit()


def check_stats(username, filename):
    '''
    Name: check_stats
    Inputs: username (string) and filename (string)
    Function: checks  player stats and displays to user on startup
    Outputs: number of times the player has played (string)
    '''
    num_plays = []

    try:
        # opens the file and checks for a number associated with user
        with open(filename, 'r') as infile:
            num_plays = infile.read()

    # if there is error because no file, only tells user no plays yet
    except OSError:
        num_plays = 0

    return num_plays

