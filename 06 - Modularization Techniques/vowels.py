"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/06/2023

Description:
    This program creates the module "vowels" that containes the functions that write the lowercase
    vowels in turtle graphics.

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


def draw_a():
    setheading(0)
    forward(50)
    pendown()
    circle(40)
    circle(40,90)
    forward(40)
    left(180)
    forward(80)
    penup()
    left(90)
    forward(20)     #Draws little a



def draw_e():
    setheading(90)
    forward(40)
    pendown()
    setheading(0)
    forward(80)
    left(90)
    circle(40,180)
    circle(40,140)
    penup()
    setheading(0)
    forward(3)
    right(90)
    forward(14)
    setheading(0)
    forward(10)     #Draws little e



def draw_i():
    forward(30)
    pendown()
    setheading(90)
    forward(80)
    penup()
    setheading(270)
    forward(80)
    left(90)
    forward(30)     #Draws little i



def draw_o():
    setheading(0)
    forward(50)
    pendown()
    circle(40)
    penup()
    forward(55)     #Draws little o



def draw_u():
    setheading(90)
    forward(40)
    pendown()
    setheading(90)
    forward(40)
    setheading(270)
    forward(45)
    circle(35,180)
    forward(45)
    left(180)
    forward(80)
    penup()
    setheading(0)
    forward(30)     #Draws little u



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
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass
    draw_e()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
