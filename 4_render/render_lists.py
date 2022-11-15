'''
    CS5001
    Spring 2020
    Homework 4 - Problem 3
    render_lists.py

    Danielle Tolliver
 
'''

P = "P"
B = "B"
L = "L"
Y = "Y"
O = "B"
R = "R"


LITTLE_IMG = [ [L, L, L, L, R, R, R, R, L, L, L, L],
               [L, L, L, R, R, R, R, R, R, L, L, L],
               [L, L, L, O, O, Y, Y, B, Y, L, L, L],
               [L, L, O, Y, B, Y, Y, B, Y, Y, Y, L],
               [L, L, O, Y, B, Y, Y, Y, B, Y, Y, Y],
               [L, L, L, O, Y, Y, Y, B, B, B, B, L],
               [L, L, L, L, Y, Y, Y, Y, Y, L, L, L],
               [L, L, L, R, R, L, R, R, L, R, L, L],
               [L, L, R, R, R, L, R, R, L, R, R, L] ]

BIG_IMG = [[P, P, P, P, P, P, P, Y, P, P, Y, Y, Y, Y, P, Y, Y, Y, P, Y, P, Y, P, P, P, P, P, P, P, Y, Y, Y], 
           [P, Y, Y, Y, Y, Y, P, Y, Y, Y, Y, Y, Y, P, Y, Y, P, Y, P, Y, P, Y, P, Y, Y, Y, Y, Y, P, Y, Y,  Y], 
           [P, Y, P, P, P, Y, P, Y, P, Y, P, P, P, Y, Y, P, Y, Y, P, Y, P, Y, P, Y, P, P, P, Y, P, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, Y, P, P, Y, Y, Y, Y, P, P, P, Y, Y, Y, P, Y, P, Y, P, P, P, Y, P, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, Y, P, P, Y, P, P, Y, Y, P, P, P, P, Y, Y, Y, P, Y, P, P, P, Y, P, Y, Y, Y], 
           [P, Y, Y, Y, Y, Y, P, Y, Y, P, Y, P, Y, Y, P, P, P, P, Y, P, Y, Y, P, Y, Y, Y, Y, Y, P, Y, Y, Y], 
           [P, P, P, P, P, P, P, Y, P, Y, P, Y, P, Y, P, Y, P, Y, P, Y, P, Y, P, P, P, P, P, P, P, Y, Y, Y], 
           [Y, Y, Y, Y, Y, Y, Y, Y, Y, P, Y, Y, P, Y, P, P, Y, Y, Y, P, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y], 
           [P, P, P, P, Y, Y, P, Y, P, Y, Y, Y, Y, P, Y, Y, Y, P, P, P, Y, P, Y, Y, P, P, P, Y, P, Y, Y, Y], 
           [P, Y, Y, Y, Y, Y, Y, Y, P, P, Y, Y, Y, Y, P, P, Y, Y, Y, P, P, P, P, P, Y, P, Y, P, Y, Y, Y, Y], 
           [Y, P, Y, P, P, Y, P, Y, Y, Y, Y, P, P, P, Y, P, P, Y, P, P, P, P, Y, P, P, P, Y, P, Y, Y, Y, Y], 
           [P, P, Y, P, P, Y, Y, Y, Y, Y, Y, P, P, P, P, P, Y, P, Y, Y, Y, Y, Y, Y, Y, Y, Y, P, Y, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, P, P, P, Y, Y, P, P, Y, P, P, Y, P, Y, P, P, Y, P, Y, Y, Y, Y, Y, Y, Y, Y], 
           [Y, P, P, P, P, P, Y, P, Y, Y, P, P, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, P, P, Y, Y, Y, Y, Y], 
           [P, P, P, Y, Y, Y, P, Y, P, Y, P, P, Y, Y, P, Y, Y, Y, P, P, P, P, P, P, P, Y, P, Y, Y, Y, Y, Y], 
           [P, Y, P, P, Y, P, Y, Y, Y, P, Y, P, Y, P, Y, Y, Y, Y, P, P, P, P, P, P, P, Y, Y, P, P, Y, Y, Y], 
           [Y, Y, P, Y, Y, Y, P, P, Y, Y, Y, P, Y, Y, P, Y, Y, Y, P, Y, Y, Y, Y, Y, P, Y, P, P, Y, Y, Y, Y], 
           [Y, P, Y, Y, Y, P, Y, P, P, Y, P, P, P, P, Y, P, Y, Y, P, P, P, P, Y, P, Y, P, Y, P, P, Y, Y, Y], 
           [P, Y, Y, P, Y, Y, P, P, Y, P, P, P, P, P, Y, Y, Y, P, Y, Y, Y, Y, Y, P, Y, P, P, P, Y, Y, Y, Y], 
           [Y, Y, Y, Y, P, Y, Y, P, Y, P, P, Y, Y, P, P, P, P, Y, Y, P, Y, P, P, Y, Y, Y, Y, P, P, Y, Y, Y], 
           [Y, P, P, Y, Y, Y, P, P, P, Y, P, Y, P, Y, P, Y, Y, Y, P, P, P, P, P, P, P, P, P, Y, P, Y, Y, Y], 
           [Y, Y, Y, Y, Y, Y, Y, Y, P, Y, P, P, P, Y, P, P, Y, Y, Y, Y, P, Y, Y, Y, P, Y, Y, P, Y, Y, Y, Y], 
           [P, P, P, P, P, P, P, Y, Y, P, P, Y, Y, P, Y, Y, Y, Y, P, P, P, Y, P, Y, P, Y, Y, P, Y, Y, Y, Y], 
           [P, Y, Y, Y, Y, Y, P, Y, Y, Y, Y, P, P, P, P, P, Y, Y, Y, Y, P, Y, Y, Y, P, Y, P, Y, Y, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, Y, Y, P, P, Y, Y, P, Y, P, Y, Y, Y, P, P, P, P, P, P, P, P, P, P, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, Y, P, P, P, Y, Y, Y, P, Y, P, P, P, Y, Y, Y, Y, Y, P, Y, P, P, Y, Y, Y, Y], 
           [P, Y, P, P, P, Y, P, Y, P, P, P, Y, Y, Y, P, P, P, P, Y, Y, Y, P, Y, P, Y, P, P, Y, P, Y, Y, Y], 
           [P, Y, Y, Y, Y, Y, P, Y, P, P, P, P, Y, P, Y, Y, P, P, P, Y, P, P, Y, P, Y, P, P, Y, P, Y, Y, Y], 
           [P, P, P, P, P, P, P, Y, P, Y, Y, P, P, Y, P, Y, P, Y, P, P, Y, Y, P, Y, Y, P, Y, P, Y, Y, Y, Y], 
           [Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y, Y]]
               
