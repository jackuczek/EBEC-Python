"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/06/2023

Description:
    This program utilized three modules: turtle, random, and (my created moduel), vowels. The program
    establishes a list of the functions from the vowel module, and then that list is shuffled so that
    order is random and no two vowels repeat. Then, a for loop is created so, for every function in
    the list, it is executed. 

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels as v
import random as r


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    vowels = [v.draw_a, v.draw_e, v.draw_i, v.draw_o, v.draw_u] #List of functions
    r.shuffle(vowels)                                           #Shuffles list so order random and nonrepeating
    for vowel in vowels:
        vowel()                                                 #Exceuted functions in shuffled list



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
