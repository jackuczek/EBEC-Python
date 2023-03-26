"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.6 - Step Counter
Date: 03/26/2023

Description:
    The program provides the user with the average number of steps per day for each month of the
    year. The program intilizes values and creates a list of month names and days of each month.
    The txt file is opened and a list is filled with each element being the number of steps in a
    day. Then, a loop is used to create the table. The month's name is spliced from the list. The
    average steps in a month is done by splicing the list of steps appropriate to the number of days
    in the month, sums the list of steps, and divided by the number of days in the month. The numbers
    are formated appropraitely and aligned.

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
    a = 0
    b = 31
    steps = []  #Initializes values and lists for better automation
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    print("The average steps taken each month were:")
    with open("steps.txt") as s:
        for line in s:
            steps.append(int(line.rstrip()))    #Creates list with step data of each day of year
    for i in range(0,12):
        print(f"{months[i]}".rjust(10),end="")
        print(" : ",end="")
        print(f"{sum(steps[a:b])/days[i]:.2f}".rjust(8))    #Splices data and divides sum by number of days in month
        a += days[i]
        if i != 11:
            b += days[i+1]      #Loops splicing of list for appropraite set for month
        else:
            pass  #Prevents index error



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
