"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 04/07/2023

Description:
    The program creates a plot of the average gas price per week over a year. The program opens the
    text file with the data, and creates two lists: weeks, with each week number starting from 1,
    and gas_prices, which is a list of weekly avg. gas prices per week from the text file. Then,
    the plot is established. The x- and y-axis limits are established, a grid background is
    created, the graph, x-axis, and y-axis titles are created, and the plot is created with the
    weeks as the x-axis and the gas_prices as the y-axis. Then, the plot is opened.

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

"""Write new functions below this line (starting with unit 4)."""


def main():
    week = 1
    gas_prices = []
    weeks = []
    with open("2008_Weekly_Gas_Averages.txt") as g:
        for line in g:
            gas_prices.append(float(line.rstrip()))
            weeks.append(week)
            week += 1                               #Makes lists of gas price/week and weeks
    fig, ax = plt.subplots()
    ax.set_xlim(1, 52)
    ax.set_ylim(1.5, 4.25)                          #Sets x- and y-axis ends
    ax.grid()                                       #Sets grid background
    ax.set_title("2008 Weekly Gas Prices")
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)") #Sets axis titles
    ax.plot(weeks,gas_prices)                       #Plots points
    plt.show()




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
