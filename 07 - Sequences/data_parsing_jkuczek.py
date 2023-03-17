"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 07.1 - Data Parsing
Date: 03/16/2023

Description:
    The program creates a table of deacades from 1950-59 to present day and the 2021 inflation-
    adjusted average price for gasoline in that decade. It parces a list of just the inflation-
    adjusted prices and creates a list of those prices. Then, the header is created, and a loop is
    used for the lines of the table. The 2020-29 decade is not part of the loop because it only
    containes two dates.

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
from data import *


"""Write new functions below this line (starting with unit 4)."""


def main():
    time = ["1950-1959", "1960-1969", "1970-1979", "1980-1989", "1990-1999", "2000-2009", "2010-2019", "2020-2029"] #List of dates
    l = []
    for i in range (3,288,4):
        l.append(data[i])                   #Creates list of inflation-adjusted prices
    j = 0
    k = 10
    m = 0
    print("          :  Price")
    print("  Decade  : in 2021")
    print("          : Dollars")
    print("-------------------")            #Formats header
    for m in range(0,7):                    #Loops that avgs prices per decade, and outputs avg price
        print(time[m] + " :  $" + str("{:.3f}".format(sum(l[j:k])/10)))
        j += 10
        k += 10
    print(time[7] + " :  $" + str("{:.3f}".format(sum(l[70:80])/2)))    #20-29 only has 2 prices, so need to adjust


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
