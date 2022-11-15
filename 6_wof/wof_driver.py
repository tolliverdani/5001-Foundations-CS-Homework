'''
    CS5001
    Spring 2020
    wof_driver.py

    Danielle Tolliver
'''
from wof_functions import *


def main():

    username = input('Enter your username to login: ')
    filename = username + '.txt'
    num_plays = check_stats(username, filename) 

    print("\nHello, ", username, ". You have played Wheel of Fortune ",
                  num_plays, " times.", sep = "")

    user_menu()


main()
