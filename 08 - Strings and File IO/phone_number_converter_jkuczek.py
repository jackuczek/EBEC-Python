"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 03/24/2023

Description:
    The program utilizes the function "convert_number" to convert a phone number than contains
    letters into numbers. The function takes the user-inputted phone number as its only argumant.
    The function capitalizes the letters in the phone number, and seperates it into a list of
    individual characters. The loop goes character by character, converting the letters into
    numbers, and does nothing to everything, and it appends each letter into a new list. The
    function then joins all the characters into the list and returns the converted phone number.
    The main function asks the user to input a phone number, the function is called to convert
    the phone number, and it prints the original and converted numbers.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
def convert_number(phone_number):
    characters = phone_number.upper()   #Capitalizes letters
    r = [*characters]                   #Seperates characters
    c = []
    for d in r:
        if d == "A" or d == "B" or d == "C":
            c.append("2")
        elif d == "D" or d == "E" or d == "F":
            c.append("3")
        elif d == "G" or d == "H" or d == "I":
            c.append("4")
        elif d == "J" or d == "K" or d == "L":
            c.append("5")
        elif d == "M" or d == "N" or d == "O":
            c.append("6")
        elif d == "P" or  d =="Q" or d == "R" or d == "S":
            c.append("7")
        elif d == "T" or d == "U" or d == "V":
            c.append("8")
        elif d == "W" or d == "X" or d == "Y" or d == "Z":
            c.append("9")
        else:
            c.append(d)                 #Loop converts letters, doesn't touch others
    return "".join(c)                   #Joins lists of converts into one number


def main():
    phone_number = str(input("Enter a telephone number: "))     #User inputs phone number
    converted_number = convert_number(phone_number)             #Function called
    print(f"  {phone_number}")
    print(f"  {converted_number}")                              #Prints original and converted numbers


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
