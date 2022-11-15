'''
    CS5001
    Spring 2020
    Homework: test_sequence.py
    Danielle Tolliver

    Starter code: sequence.py

    The starter code linked above defines two functions: one to compute the kth
    term of an arithmetic sequence, and one to compute the sum of the first n
    terms of an arithmetic sequence.

    Your job is to test these functions. You should write a main in
    test_sequence.py; when I run it, I should see all of your exhaustive tests,
    the expected result for each one, and the actual result for each one.
    
'''

from sequence import kth_term
from sequence import arith_sum


def report_results(initial, diff, n, expected, actual):
    '''
    Function: report_results
    Parameters: 4 integers; number we're taking apart, n to give the place
    10^n, expected result, and the actual result
    Returns: Nothing; calls the get_digit function and prints actual vs
    expected result
    '''
    print("\nInitial: ", initial, "\n",
          "Difference: ", diff, "\n"
          "N: ", n, "\n",
          "Expected: ", expected, "\n",
          "Actual: ", actual, sep="")


def test_arith_sum(initial, diff, n, expected):
    '''
    Function: test_arith_sum
    Parameters: 3 integers; a number whose digits we want to isolate,
    n to get 10^n place, and the expected result from calling get_digit
    Returns: nothing, calls the report_results function to see what happened
    '''
    actual = int(arith_sum(initial, diff, n))
    report_results(initial, diff, n, expected, actual)


def main():

    #Test 1 - my static inputs
    test_arith_sum(20, 40, 2, 80)
    test_arith_sum(100, 50, 5, 1000)
    test_arith_sum(0, 10, 5, 100)
    test_arith_sum(-100, -50, 5, -1000)
    test_arith_sum(0, -10, -5, -150)

    #Test 2 - get inputs from the user
    print("\nNow you try!\n")
    test_initial = int(input("Tell me the initial number: "))
    test_diff = int(input("Tell me the diff: "))
    test_n = int(input("Tell me N: "))
    test_expected = int(input("Tell me what you expect: "))

    test_arith_sum(test_initial, test_diff, test_n, test_expected)

main()
