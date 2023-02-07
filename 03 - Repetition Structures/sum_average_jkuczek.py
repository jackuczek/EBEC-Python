"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 03.2 - Sum Average
Date: 02/07/2023

Description:
    The program assignes the sum and count initially as 0. The program asks the user to input a
    number. The inputted number goes towards the sum and the count goes up by 1. The program
    asks the user to input another number and stops asking when the user inputs a negative
    number. When a negative number is inputted, it formats the count and tells the user
    how many numbers are inputted. It calculates the average, formats the average and sum, and
    outputs it. If only a negative number is inputed, it tells the user no numbers were
    inputted.

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
    msg = "Enter a non-negative number (negative to quit): "
    count, sum = 0, 0                                                                       #Count & sum starts at 0
    num = float(input(msg))                                                                 #Num is what user inputs
    while num >= 0:
        count += 1
        sum += num
        num = float(input(msg))                                                             #While number inputed > 0, adds to count and asks again
    if sum > 0:
        fcount = int(count)
        print("  You entered " + str(fcount) + " numbers.")
        avg = sum/count
        fsum = "{:.3f}".format(sum)
        favg = "{:.3f}".format(avg) 
        print("  Their sum is " + str(fsum) + " and their average is " + str(favg) + ".")    #If sum greater then 0, calculates, formats, and outputs sum and avg
    else:
        print("  You didn't enter any numbers.")                                             #If only num < 0 input, then says no num inputed


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
