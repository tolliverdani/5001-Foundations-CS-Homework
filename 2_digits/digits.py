'''
    CS5001
    Spring 2020
    Homework: digits.py
    Danielle Tolliver

    Starter code: test_digits.py

    --
    
    Got information about math.fabs() so it will work on neg numbers from here:
    https://docs.python.org/2/library/math.html
    
'''

import math

def get_digit(value, power):
    ''' Function get_digit
        Parameters: 2 integers; number to take apart and n to give place 10^n
        Returns: a single integer from the nth place of the original integer
        Output: the digit (int)
    '''
    calc_value = math.fabs(value)

    #finds the values of the power
    calc_power = 10 ** (power + 1)
    new_power = 10 ** (power)

    #find the upper limit
    high_value = calc_value % (new_power)
    high_number = value - high_value

    #find the lower limit
    low_value = calc_value % (calc_power)
    low_number = value - low_value

    #singles out the digit
    digit = high_number - low_number
    digit = int(digit / new_power)

    return digit
