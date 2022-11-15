'''
    CS5001
    Spring 2020
    Homework: rent.py
    Danielle Tolliver
    
    We all know that 525,600 minutes is how we measure, measure a year. But let’s measure it
    better! Write a program that prompts the user for a number of minutes (a float), and breaks
    that value in terms of:
    
    Years
    Days 
    Hours
    Minutes
    Seconds

    This is called an optimization problem. We could turn any input into all seconds, and
    that’s technically correct -- it does break down the original time. But, it’s not what
    we’re going for here; instead, we want to break down the most possible years, months, etc.

    Because the user enters a float for minutes, remember to do the conversion to seconds
    correctly 1.5 minutes is one minute and 30 minutes (not one minute and 50 seconds). 

    Before you begin coding -- write test cases!
    In the comments at the top of your Python file, list 3 test cases that you came up with
    (which you devised before you began writing your code). 

    Test case #1 (to get the idea right):
    Input: 525600
    Years: 1

    Test case #2:
    Input:   23456789765.5
    Years:   44628
    Days:    217
    Hours:   8
    Minutes: 5
    Seconds: 30

    Test case #3:
    Input:   76543234567.9372
    Years:   145630
    Days:    74
    Hours:   0
    Minutes: 7
    Seconds: 56 
'''

import math

def main():

    #Get input from user and store as a float variable
    minutes = float(input("Please enter the number of minutes to convert: \n"))

    #Calculate years
    years = minutes / 525600
    remaining_years = years - math.floor(years)

    #Calculate days
    days = remaining_years * 365
    remaining_days = days - math.floor(days)    

    #Calculate hours
    hours = remaining_days * 24
    remaining_hours = hours - math.floor(hours)

    #Calculate minutes
    minutes = remaining_hours * 60
    remaining_minutes = minutes - math.floor(minutes)

    #Calculate seconds
    seconds = remaining_minutes * 60

    #Print the values for the user
    print("That is...\n",
          math.floor(years), "years,\n",
          math.floor(days), "days,\n",
          math.floor(hours), "hours,\n",
          math.floor(minutes), "minutes,\n",
          "and", round(seconds), "seconds.")


main()
