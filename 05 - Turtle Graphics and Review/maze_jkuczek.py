"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 05.1 - Maze
Date: 02/26/2023

Description:
    The program lists the movements the turtle needs to make so that is can solve the maze, starting
    from the center and exiting to the right.

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
from turtle import *        #Imports turtle graphics

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)            #Initial conditions of turtle


def main():
    left(90)
    forward(12)
    right(90)
    forward(36)
    left(90)
    forward(72)
    right(90)
    forward(24)
    left(90)
    forward(48)
    right(90)
    forward(96)
    right(90)
    forward(96)
    right(90)
    forward(48)
    left(90)
    forward(96)
    left(90)
    forward(24)
    right(90)
    forward(24)
    left(90)
    forward(96)
    left(90)
    forward(84)
    right(90)
    forward(24)         #Directions so the turtle solves the maze


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
