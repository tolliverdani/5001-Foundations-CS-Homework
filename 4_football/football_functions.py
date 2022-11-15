'''
    CS5001
    Spring 2020
    Homework 4 - Problem 1
    football_functions.py

    Danielle Tolliver

    --
    
    Learned how to remove [] and '' using this link:
    https://stackoverflow.com/questions/3900054/python-strip
    -multiple-characters
    
'''

def count_result(results, outcome):
    '''
    Name: count_restul
    Inputs: list of W/L/D, string for outcome.
    Function: number of games with an outcome
    Outputs: number of games (int)
    '''
    total = 0
    
    for i in range(len(results)):

        if results[i] == str(outcome):
            total += 1
    return(total)


def count_one_wins(results, goals):
    '''
    Name: count_one_wins
    Inputs: list of W/L/D; list of ints with the number of goals per game
    Function: counts the number of games won with only one goal
    Outputs: number of games (int)
    '''
    total = 0
    
    for i in range(len(results)):

        if results[i] == "W":

            if goals[i] == 1:
                total += 1

    return(total)


def compile_streaks(results):
    '''
    Name: compile_streaks
    Inputs: list of W/L/D
    Function: takes the string and counts consecutive responses
    Outputs: streaks for whole season, like "1W 1L 1D 1W 1D 4W" (string)
    '''
    streak = []
    
    if len(results) == 0:

        return("")

    elif len(results) == 1:

        streak.append("1"+str(results[0]))

    else:
        
        current_count = 1
    
        for i in range(1, len(results)):

            if results[i-1] == str(results[i]):
                current_count += 1
            
            else:
                streak.append(str(current_count)+str(results[i-1]))
                current_count = 1

        streak.append(str(current_count)+str(results[i]))

    return(str(streak).replace("', '"," ").strip("''").strip("[]").strip("''"))


def sum_points(results, season, game_number):
    '''
    Name: sum_points
    Inputs: list of W/L/D; two ints s and n
    Function: totals the number of points after nth game of season s
    Outputs: the number of points (int)
    '''
    total_points = 0
    
    for i in range(game_number):

        if results[i] == "W":
            total_points += 3

        elif results[i] == "D":
            total_points += 1

    return(total_points)
