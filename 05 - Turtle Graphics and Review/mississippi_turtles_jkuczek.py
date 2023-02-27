"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 02/27/2023

Description:
    This program should have been able to draw the term "Mississippi turtles" using the turtle python
    library. However, I was unable to firgure it out and gave up. 

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
    setup(600, 400)
    width(9)
    color("purple")


def draw_e():
    penup()
    goto(0,30)
    pendown()
    forward(60)
    left(90)
    circle(30, 315)
    penup()
    goto(60,0)

def draw_i():
    penup()
    goto(30,0)
    left(90)
    pendown()
    forward(60)
    penup()
    forward(30)
    pendown()
    forward(1)
    penup()
    goto(60,0)


def draw_l():
    penup()
    goto(30,0)
    left(90)
    pendown()
    forward(120)
    penup()
    goto(60,0)


def draw_M():
    penup()
    goto(60,0)
    left(90)
    pendown()
    forward(90)
    circle(15,180)
    forward(90)
    backward(90)
    left(180)
    circle(15,180)
    forward(90)
    penup()
    goto(60,0)

def draw_p():
    penup()
    goto(0,60)
    pendown()
    right(90)
    forward(120)
    penup()
    goto(0,30)
    pendown()
    circle(30)


def draw_r():
    penup()
    goto(0, 0)
    pendown()
    left(90)
    forward(60)
    backward(25)
    circle(-20, 120)
    penup()
    goto(60, 0)

def draw_s():
    penup()
    goto(0, 0)
    pendown()
    backward(15)
    forward(15)
    circle(15, 180)
    circle(-15, 180)
    forward(10)


def draw_t():
    penup()
    goto(30,0)
    left(90)
    pendown()
    forward(120)
    penup()
    goto(0,80)
    right(90)
    pendown()
    forward(60)


def draw_u():
    penup()
    goto(-50, 0)
    pendown()
    right(90)
    forward(60)
    circle(30, 180)
    forward(60)
    backward(90)        #Functions for drawing necessary letters


def main():
    draw_M()        #Draws "Mississippi Turtles"
    draw_i()
    draw_s()
    draw_s()        #Unable to complete



"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
