"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 02.1 - Leap Year
Date: 01/30/2004

Description:
    The program asks the user to input a year and it outputs whether or not the provided year is a leap
    year, and how many days is in the year. For a year to be a leap year, it must either be divisible by
    100 and 400, and, if it is not divisisble by 100, then it must be divisible by 4. If it fails those
    two tests, then the given year is not a leap year.

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
    year = float(input("Enter a year: "))                                   #Asks user to input year
    if year%100 == 0 and year%400 == 0:
        print("The year " + str(int(year)) + " is a leap year.")
        print("February of " + str(int(year)) + " has 29 days.")            #If year divisible by 100 and 400, then leap year
    elif year%100 != 0 and year%4 == 0:
        print("The year " + str(int(year)) + " is a leap year.")
        print("February of " + str(int(year)) + " has 29 days.")            #If year not divisible by 100 but is by 4, then leap year
    else:
        print("The year " + str(int(year)) + " is not a leap year.")
        print("February of " + str(int(year)) + " has 28 days.")            #Else, not leap year
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
