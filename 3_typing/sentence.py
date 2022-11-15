'''
    CS5001
    Spring 2020
    Homework 3 - Problem 3
    sentence.py

    Danielle Tolliver

    Contains modified sentences from original starter document
    
'''

import time
import random

PHRASES = ["Handing Lady: Nervous? Ted Striker: Yes. Very. Handing Lady: First time? Ted Striker: No, I've been nervous lots of times.",
           "Ted Striker: Surely you can't be serious. Dr. Rumack: I am serious...and don't call me Shirley.",
           "Ted Striker: Looks like the foot is on the other hand now, Mr. Kramer!",
           "Ted Striker: These people need to go to a hospital. Elaine Dickinson: What is it? Ted Striker: It's a big place where sick people go",
           "Kramer: No... that's just what they'll be expecting us to do!",
           "Light travels faster than sound. That's why some people appear bright until you hear them speak.",
           "I was wondering why the ball was getting bigger. Then it hit me."
           "I have a few jokes about unemployed people, but none of them work.",
           "When life gives you melons, you're dyslexic.",
           "I Renamed my iPod The Titanic, so when I plug it in, it says The Titanic is syncing",
           "It's hard to explain puns to kleptomaniacs because they always take things literally.",
           "I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over.",
           "Two windmills are standing in a wind farm. One asks, What’s your favorite kind of music? The other says, I’m a big metal fan.",
           "Did you hear about the guy whose whole left side was cut off? He’s all right now.",
           "What do you call a bee that can’t make up its mind? A maybe.",
           "A police officer just knocked on my door and told me my dogs are chasing people on bikes. That’s ridiculous. My dogs don’t even own bikes.",
           "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it.",
           "Hello, my name is Inigo Montoya. You killed my father. Prepare to die.",
           "It’s bullshit, I did not hit her. I did nooot. Oh hi, Mark!",
           "You're tearing me apart, Lisa!",
           "We don't make mistakes, just happy little accidents.",
           "Talent is a pursued interest. Anything that you're willing to practice, you can do.",
           "One morning I shot an elephant in my pajamas. How he got into my pajamas I'll never know.",
           "The complex houses married and single soldiers and their families.",
           "I want to be the very best, like no one ever was. To catch them is my real test, to train them is my cause!",
           "socrates: to do is to be, plato: to be is to do, scooby: do be do.",
           "Therapist: And what do we say when we feel like this? Me: It be like that sometimes Therapist: No",
           "All the things I really like to do are either immoral, illegal or fattening.",
           "At every party there are two kinds of people – those who want to go home and those who don’t. The trouble is, they are usually married to each other.",
           "To be sure of hitting the target, shoot first, and call whatever you hit the target.",
           "Facebook just sounds like a drag, in my day seeing pictures of peoples vacations was considered a punishment.",
           "Money won’t buy happiness, but it will pay the salaries of a large research staff to study the problem.",
           "Laughing at our mistakes can lengthen our own life. Laughing at someone else’s can shorten it.",
           "Remember, today is the tomorrow you worried about yesterday.",
           "I am wet when drying. What am I?",
           "How far can a raccoon run into the woods?"]

def select_sentence():
    ''' Function select_sentence
        Input: nothing
        Returns: a randomly-chosen sentence from the list above (string)
    '''
    return random.choice(PHRASES)

def count_words(sentence):
    ''' Function count_words
        Input: a string
        Returns: an int, the number of words in the given string.
                 Uses one white space as a delimiter, nothing else.
    '''
    words = sentence.split(' ')
    return len(words)

def count_mismatches(phrase_one, phrase_two):
    ''' Function count_mismatches
        Input: two strings for comparison
        Returns: an int, the number of differences between the two strings.
                 We count differences in each word (not each character).
                 If the words at position i in each sentence differ at ALL,
                 case included, that's a mismatch.
                 If one sentence is longer than the other, each extra word
                 it has is also a mismatch.
    '''
    list_one = phrase_one.split(' ')
    list_two = phrase_two.split(' ')
    min_length = min(len(list_one), len(list_two))

    # Count the position-by-position mismatches
    errors = 0
    for i in range(min_length):
        if list_one[i] != list_two[i]:
            errors += 1

    # Add on any mismatches if one phrase was longer
    errors += abs(len(list_one) - len(list_two))

    return errors
    
           
