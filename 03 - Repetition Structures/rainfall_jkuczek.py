"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 03.3 - Rainfall
Date: 02/12/2023

Description:
    The program asks the user to input the number of years the rainfall is being accounted for. The
    count starts at 1, and lists for the months and rainfall amounts are established. If the number
    of years inputted is less than 0, the program says that the input is invalid and ends the
    program. Else, the program asks the the amount of rain for each month and adds the amount to
    the list. If the amount inputted is less than 0, it says the amount is invalid and asks the user
    to input the amount again. One the loops are done, it tells the user how many months are
    accounted for, tells the user the sum of all the amount (to two decimal places), and tells the
    user the average amount of rain per month (to two decimal places).

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    years = int(input("Enter the number of years: "))                           #User inputs years
    count = 1
    lmonths = ['Jan.: ', 'Feb.: ', 'Mar.: ', 'Apr.: ', 'May.: ', 'Jun.: ', 'Jul.: ', 'Aug.: ', 'Sep.: ', 'Oct.: ', 'Nov.: ', 'Dec.: ']
    lrain = []                                                                  #Establishes lists
    if years <= 0:
        print("Invalid input; years must be greater than 0.")                   #If years<0, program ends
    else:
        while count < years+1:
            print("  For year No. " + str(count))                               #Goes through every year
            for m in lmonths:
                rain = float(input("    Enter the rainfall for " + m))          #Goes through every month
                while rain < 0:
                    print("    Invalid input; rainfall cannot be negative.")
                    rain = eval(input("    Enter the rainfall for " + m))       #Reasks user for rain if rain<0
                else:
                    lrain.append(rain)                                          #Adds rain to list
            count += 1
        print("There are " + str(years*12) + " months.")
        total = sum(lrain)
        ftotal = "{:,.2f}".format(total)
        print("The total rainfall was " + str(ftotal) + " inches.")             #Sums and formats list of rain
        avg = total/(years*12)
        favg = "{:,.2f}".format(avg)
        print("The monthly average rainfall was " + str(favg) + " inches.")     #Avgs and forms avg rainfall




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
