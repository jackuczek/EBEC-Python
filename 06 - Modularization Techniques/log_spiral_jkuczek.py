"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 03/05/2023

Description:
    The program initially places the turtle at the initial point of the spiral (4,0), given by the
    fact that a. I set the variables as theta=i=0, a=4, and b=.22. The loop converts i to radians,
    finds the Cartesian coordinates of the spiral, and the turtle plots the coordinates, and i
    increases by 1. The loop continues until i = 1080+1 to create the full spiral.

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
from turtle import *
from math import *


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    penup()
    goto(4,0)
    pendown()
    i = 0
    a = 4
    b = 0.22                    #Initializes variables
    while i in range(1080+1):
        r = i*pi/180            #Converts degrees to radians
        x = a*exp(b*r)*cos(r)
        y = a*exp(b*r)*sin(r)   #Converts to Cartesian coordinates
        goto(x,y)               #Draws
        i += 1                  #Steps of 5


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
