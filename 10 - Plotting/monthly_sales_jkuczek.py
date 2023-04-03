"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 04/03/2023

Description:
    The program constructs a pie chart of the sales volume per month in a year. The user inputs the
    sales volume in each month via a loop. The sales they input is added to a list. Then, using 
    matplotlib, a plot is constrcuted. It is titled "Monthly Sales Values." The variable is the sales
    volume, the colors for each month is provided in hexadecimal, and the labels for each slice are
    the months.

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
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    sales = []
    for month in months:
        sale = int(input(f"Enter the sales for {month}: "))
        sales.append(sale)      #User inputs sales in months and is added to list
    fig, ax = plt.subplots()
    ax.set_title("Monthly Sales Values")    #Title is set
    y = sales   #Variable is sales amt
    c = ["#4D4038", "#BAA892", "#5B6870", "#6E99B4", "#A3D6D7", "#085C11", "#849E2A", "#C3BE0B", "#E9E45B", "#6B4536", "#B46012", "#FF9B1A"]    #Color in hex
    l = months  #Label is months
    ax.pie(y, colors=c, labels=l)       #Pie chart constructed using specififcations
    plt.show()      #Pie chart is shown

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
