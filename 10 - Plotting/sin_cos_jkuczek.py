"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 04/03/2023

Description:
    This program plots a sine and cosine curve using matplotlib and numpy. A plot is first
    established. A range of x values is also extablished. The y range fo rthe sine and cosine
    curves are created using the numpy cos and sin functions according to the assignment's
    specifications. The sine curve is red and the cosine curve is blue. The x and y limits are just
    around the required so that it matches the basis in the assignment. Ticks are made and labeled
    according to assignment specifications. Spines are used to print the x-axis to the middle of
    the plot. Then, the plot is shown.

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
import matplotlib.pyplot as plt
from numpy import *

"""Write new functions below this line (starting with unit 4)."""


def main():
    fig, ax = plt.subplots()
    x = arange(0, 2*pi, 0.01)   #X range for sine and cosine
    sine = sin(x**2)
    cosine = cos(x)**2      #Y range for sine and cosine
    ax.plot(x,sine,color = "red")
    ax.plot(x,cosine,color = "blue")    #Plots sine and cosine waves
    ax.set_xlim(-.1,2.1*pi)
    ax.set_ylim(-1.1,1.1)   #Range of x- and y-axis
    ax.set_xticks([pi/2,pi,3*pi/2,2*pi])
    ax.set_yticks([-1,1])   #Ticks for x- and y- axis
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])
    ax.set_yticklabels(["−1","1"])  #Tick labels for x- and y-axis
    for spine in ['top','right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')   #Proper axis formatting
    plt.show()  #Shows graph


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
