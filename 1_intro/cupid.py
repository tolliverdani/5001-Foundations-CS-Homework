'''
    CS5001
    Spring 2020
    Homework: cupid.py
    Danielle Tolliver

    Prompt the user for all the important stats you’d want on a dating site profile,
    and display them back to the user.

    Prompt the user for:

        First name
        Last name
        Age
        Annual income
        Number of dogs
        Team Jacob or Team Edward

    You can assume that the user enters valid information.
    You should treat each input variable as the appropriate data type.

    ---
    
    Got formatting help for annual income here: https://www.reddit.com/r/learnpython/comments/45c9kw/adding_or_in_python_without_space_in_between_the/
'''

def main():

    #Get inputs from user and store as variables (income is a float)
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    age = input("What is your age?\n")
    income = float(input("What is your annual income?\n"))
    dogs = input("How many dogs do you have?\n")
    team = input("Which man in Twilight do you prefer: Edward or Jacob?\n")

    #Print thank you message and all of the values for the user
    print("\nThank you for your profile information! Here's what we stored for you.\n",
          "\nFirst name:", first_name,
          "\nLast name:", last_name,
          "\nAge:", age,
          "\nAnnual income:", '${:.2f}'.format(income),
          "\nNumber of dogs:", dogs,
          "\nYou are on team:", team)
    
main()
