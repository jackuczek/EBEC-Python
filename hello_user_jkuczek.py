"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 00.1 - Hello User
Date: 01/11/2023

Description:
    This program asks the user's name, which is an input that is assigned the variable name "name", by asking
    the user "What is your name?" This outputs "Hello [name]!" using the function "print."
    Simply, the programs asks the user's name as an input, and outputs "Hello [user's name]!"

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


def main():
    name = input("What is your name? ")     #Asks user to input their name and is assigned as "input"
    print("Hello " + name + "!")            #Prints "Hello [name]!", where [name] is whatever the user inputed

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
