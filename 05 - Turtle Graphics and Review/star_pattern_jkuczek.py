"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 02/26/2023

Description:
    The program draws a star according to the users input. The user inputs a desired number of points
    the star would have. The program does some calculations for the angles of the star. The program
    begins a fill color for the star, and the turtle is orientated approperiately so the star has
    the correct orientation. Then, there's a loop for each point of the star, that repeats equal to
    the number of the points of the star. When the loop is completed. The star is filled in with the
    color blue.

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

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    points = int(input("How many points do you want on the star? "))    #Asks user for # of points
    A = 360/points
    B = 2*A
    i = 1
    fillcolor("#256D7B")
    begin_fill()                                                        #Fill color is blie
    right(90-B/2)                                                       #Initial turtle orientation
    while i <= points:
        forward(60)
        right(A-180)
        forward(60)
        left(B-180)
        i += 1                                                          #Loop for each point of star
    end_fill()

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
