'''
    CS5001
    Spring 2020
    Homework: currency.py
    Danielle Tolliver

    Cheesy Joe’s Currency Exchange converts US Dollars to Wizarding Money.
    For each conversion, they charge a flat fee plus 3% of the amount converted.
    For instance, the total charge for converting 350 U.S. dollars is .03 * 350 + fee = $15.00 

    Write a program that prompts the user for a US currency value, and tells them the total
    amount charged to do the conversion. (Part of your job is to figure out the flat fee.)

    Your output should be formatted the way we’d expect currency to look, like this: $100.00.
    You can assume that the user enters a valid input, and you should treat it as a float.

    Math for the flat fee:
    .03 * 350 + fee = 15
    .03 * 350 = 10.5
    15 - 10.5 = fee
    4.5 = fee

    Test case #1:
    Input: 300
    Total fee: $13.50

    Test case #2
    Input: 100
    Total fee: $7.50

    Test case #3
    Input: 750
    Total fee: $27.00

    ---
    
    Got formatting help for annual income here: https://www.reddit.com/r/learnpython/comments/45c9kw/adding_or_in_python_without_space_in_between_the/
'''

#Store flat fee as a constant variable
flat_fee = 4.50
    
def main():

    #Get input from user and store as a float variable
    amount = float(input("Please enter the amount to convert: "))

    #Calculate total fee
    fee = amount * .03
    total_fee = fee + flat_fee

    #Print the value for the user
    print("Cheesy Joe's charges you:",'${:.2f}'.format(total_fee))

main()
