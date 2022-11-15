'''
    CS5001
    Spring 2020
    Homework 4 - Problem 2
    compress_funcitons.py

    Danielle Tolliver
 
    --
    
    Learned how to remove [] and '' using this link:
    https://stackoverflow.com/questions/3900054/python-strip
    -multiple-characters
    
'''

import copy
import math

ROWS = 3
COLUMNS = 4
PIXELS_PER_PAGE = ROWS * COLUMNS

P = "P"
L = "L"
G = "G"
W = "W"
Y = "Y"

image_1 = [[P, P, P, P, G, G, G, G],	   
                 [P, G, G, G, Y, Y, L, L],
                 [L, L, L, L, P, P, L, L], 
                 [L, L, P, P, L, L, L, L],
                 [W, W, W, W, L, L, L, L],
                 [W, G, G, G, L, L, P, P]]

image_2 = [[P, P, P, P],
               [P, G, G, G],
               [L, L, L, L],
               [L, L, P, P],
               [W, W, W, W],
               [W, G, G, G]]


def compress(image):
    ''''
    Name: compress
    Inputs: image (list)
    Function: takes the image (list) and counts color streaks
    Returns: a string of streaks (string)
    '''
    compressed = compress_first(image)
    streak = []

    # if there is nothing, return nothing
    if len(compressed) == 0:

        return(streak)

    else:

        temp_streak = []

        # for each row
        for i in range(len(compressed)):

            # define / reset temp_streak to empty and count to 1
            temp_streak = []
            current_count = 1
            
            # for each element in row...
            for j in range(1, len(compressed[i])):
                                                  
                # if the previous elem is same as current, increase count
                if str(compressed[i][j-1]) == str(compressed[i][j]):
                    current_count += 1

                else:                
                    
                    # otherwise save count and color to temp_streak
                    temp_streak.append(str(current_count)+" "
                                       +str(compressed[i][j-1]))

                    # and reset counter to 1
                    current_count = 1

            # at the end of row, add last elem to temp_list
            temp_streak.append(str(current_count)+" "
                               +str(compressed[i][j-1]))
 
            # then add temp_streak to the list 'streak'
            streak.append(temp_streak)
        
        return(streak)


def compress_first(image):
    '''
    Name: compress_first
    Inputs: original_image (list)
    Function: takes orginal list and chunks into pages worth of pixels
    Output: list(s) within list (list)
    '''
    compressed = []
    pages = int(num_pages(image))
    c_multiplier = int(column_multiplier(image))
    r_multiplier = int(row_multiplier(image))

    #print("pages:", pages, "c_m:", c_multiplier, "r_m:", r_multiplier)
    
    # for each page...
    for p in range(pages):

        #print("p:", p)
        
        # define / reset temp_list to empty
        temp_list = []

        # for each row...
        for i in range(ROWS):

            row_location = i

            if p == 1:

                # calculate row adjustments based on page number
                row_location = int(math.ceil(p / r_multiplier) * ROWS) + i

            if p >= 2:

                # calculate row adjustments based on page number
                row_location = int(math.floor(p / r_multiplier) * ROWS) + i

            # and for each column...
            for j in range(COLUMNS):

                # if p is an odd page...
                if p % 2 != 0:

                    # calculate column adjustments
                    column_location = int(math.floor(c_multiplier / 2) * COLUMNS) + j
                    pixel = image[row_location][column_location]
                    #print("i:", row_location, "j:", j, "cl:", column_location, "rl:", row_location)

                    # add pixel to temp_list
                    temp_list.append(pixel)

                else:

                    # no need for column adjustments
                    column_location = j
                    pixel = image[row_location][column_location]
                    #print("i:", row_location, "j:", j, "cl:", column_location, "rl:", row_location)

                    # add pixel to temp_list
                    temp_list.append(pixel)
               
        # add the temp_list to list 'compressed' before resetting to empty
        compressed.append(temp_list)
                
    return(compressed)


def column_multiplier(image):

    count_elements = 0
    
    for i in range(len(image)):
        for j in range(len(image[i])):
            count_elements += 1

    count_columns = count_elements / len(image)
    multiplier = int(count_columns / COLUMNS)
    
    return(multiplier)


def row_multiplier(image):

    count_rows = 0
    
    for i in range(len(image)):
            count_rows += 1

    multiplier = int(count_rows / ROWS)
    
    return(multiplier)


def num_pages(image):
    '''
    Name: num_pages
    Inputs: original_image (list)
    Function: takes orginal list and calculates number of pages
    Output: num_pages (int)
    '''
    # counts number of pages for output and returns it as an int
    num_pages = math.ceil(len(image) * len(image[0]) / PIXELS_PER_PAGE)

    return(num_pages)


def main():
   
    print(compress(image_1))
    print(compress(image_2))

main()
