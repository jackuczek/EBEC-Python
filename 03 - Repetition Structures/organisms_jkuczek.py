"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 03.4 - Organisms
Date: 02/10/2023

Description:
    This program outputs the growth of a population given user input. The program asks the user to input the count of the starting population in thousands,
    the rate of increase in percent, and the number of days the population with grow. The program establishes two lists: days and population (pop). The first
    two entries for the "days" list is the heading "Days" and the value 0, because the days will always start at 0. The first two entires of the "pop" list
    is the heading "Approx. Pop" and the formatted value for the starting population that user has inputed. Then, the program adds 1 to the count and
    calculates the increase in population using the given equation. The programs formats the new count and new population, and adds them to the end of their
    respective lists. The new population is then equal to the variable name "start" to establish a recursive sequence. This loop countinues while the
    count is less than the number of day the user inputed. The last two lines makes the list into right-alligned columns, making it nice and fancy.

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
    start = float(input("Starting population, in thousands: "))
    rate = float(input("Average daily increase, in percent: "))
    days = float(input("Number of days to multiply: "))                 #User input for initial pop, rate, and # of days
    count = 0
    istart = "{:,.3f}".format(start)                                    #Formatting values for day=0
    day = ["Day", 0]
    pop = ["Approx. Pop", str(istart)]                                  #Begins lists
    while count < days:
        count += 1
        newpop = start*(1+(rate/100))                                   #Eqn for new pop
        fnewpop = "{:,.3f}".format(newpop)
        day.append(int(count))
        pop.append(fnewpop)                                             #Adds value to list
        start = newpop                                                  #Establishes recursive series
    for j in range(0,len(day)):
        print(f"{day[j]:>3}   {pop[j]:>11}")                            #Prints two lists into two right-alligned columns


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
