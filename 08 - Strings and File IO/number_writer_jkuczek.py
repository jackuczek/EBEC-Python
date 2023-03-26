"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.4 - Number Writer
Date: 03/26/2023

Description:
    The program creates a text file with a list of numbers that are within the bounds of [1019,1217],
    but is not 1025, 1042, or 1188. The program asks the user for an input on the number of numbers
    it should write. Then, there's a loop that repeats the number of times the user has inputted,
    wherea random integer is chosen, if it is one of the excluded numbers, it redos the random
    choice, and adds the number to a list of strings that includes "\n", so a new line is printed.
    Then, the program writes the list as lines, completed the text file with a user-specified number
    of numbers.

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
from random import *


"""Write new functions below this line (starting with unit 4)."""


def main():
    print("This program will fill a file with random numbers.")
    count = int(input("How many numbers should it write? "))    #User inputs amt of numbers in txt file
    l = []
    exclude = [1025,1042,1188]
    for i in range(1,count+1):
        n = randint(1019,1217)          #Random integer within given bounds
        while n in exclude:
            n = randint(1019, 1217)     #If number is one of excluded, redo
        l.append(f"{n}\n")              #Add number to list
    with open('random_numbers.txt', 'w') as r:
        r.writelines(l)                 #Prints list as lines


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
