"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 05.2 - Hex Spiral
Date: 02/26/2023

Description:
    The program draws a hexagon spiral using a loop. The program sets the initial length of the side
    to n = 6. Then, there's the loop. In the loop, the cursor moves forward n, turns 60 degress, and
    the n increases by 6. This loops 39 times, which is when the give shape is made.

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
    width(5)


def main():
    n = 6                   #Sets initial length to 6
    for i in range(1,40):
        forward(n)
        right(60)           #Draws line and turns 60
        n = n + 6           #Increases length by 6 each loop

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
