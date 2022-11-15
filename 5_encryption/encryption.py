'''
    CS5001
    Spring 2020
    Homework 5 - Problem 1
    encryption.py

    Danielle Tolliver

    Encrypted messages:
    1. the man who passes the sentence should swing the sword
    2. everyone is mine to torment
    3. you know nothing, jon snow
    4. that's what i do: i drink and i know things

    Your turn!
    1. tuznotm muky ubkx se nkgj. se xklrkdky gxk zuu lgyz. o cuarj igzin oz.
    2. fqtocoow, k’xg eqog vq dctickp.
    3. csy ger hs mx. csy ger hs ercxlmrk. csy’vi xli asvph’w kviexiwx kverhqe.
    
'''

def decrypt(user_input, shift):
    '''
    Name: decrypt
    Inputs: user_input (string) and shift (int)
    Function: takes the user_input and shifts letters backward by shift amount
    Output: decrypted_message (string)
    '''
    # ensures the shift is within 0 to 25
    if shift < 0:
        shift = 1

    elif shift > 25:
        shift = 1

    # takes the user_input and makes it lower case
    user_input = user_input.lower()

    # creates an empty string to put new sentence into
    decrypted_mesage = ""

    # for each character in the string
    for char in user_input:

        # this only converts alphabetic characters 
        if (ord(char) <= 122 and ord(char) >= 97):
            
            char = chr((ord(char) - shift - 97) % 26 + 97)
            decrypted_mesage += char

        #if it's not an alphabetic character then keep it the same
        else:

            decrypted_mesage += char
        
    return(decrypted_mesage)


def encrypt(user_input, shift):
    '''
    Name: encrypt
    Inputs: user_input (string) and shift (int)
    Function: takes the user_input and shifts each letter by the shift amount
    Output: encrypted_message (string)
    '''
    # ensures the shift is within 0 to 25
    if shift < 0:
        shift = 1

    elif shift > 25:
        shift = 1

    # takes the user_input and makes it lower case
    user_input = user_input.lower()

    # creates an empty string to put new sentence into
    encrypted_mesage = ""

    # for each character in the string
    for char in user_input:
        
        # this only converts alphabetic characters 
        if (ord(char) <= 122 and ord(char) >= 97):

            char = chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_mesage += char

        #if it's not an alphabetic character then keep it the same
        else:

            encrypted_mesage += char
       
    return(encrypted_mesage)
