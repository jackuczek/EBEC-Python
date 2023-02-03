"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 02/03/2023

Description:
    This program asks the user to input a number that is on a roulette wheel. If the user inputs a
    number that is not on a roulette wheel, the program will says that is an invalid input. If the
    number is 0, then the program says the pocket is green. If the the number is from 1 to 10 or
    from 19 to 28, an even number's pocket is black and an odd number's pocket is red. If the
    number is from 11 to 18 or from 29 to 36, an even number's pocket is red and an odd number's
    pocket is black.

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
    pocket = float(input("Please choose a pocket number: "))                 #Asks for pocket
    if pocket < 0 or pocket > 36:
        print("  Invalid Input!")                                            #If number not on wheel, invalid
    elif pocket == 0:
        print("  Pocket number " + str(int(pocket)) + " is green.")          #If 0, green
    elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
        if pocket%2 == 0:
            print("  Pocket number " + str(int(pocket)) + " is black.")
        else:
            print("  Pocket number " + str(int(pocket)) + " is red.")        #For this subset, even=black, odd=red
    elif 11 <= pocket <= 18 or 29 <= pocket <= 36:
        if pocket%2 == 0:
            print("  Pocket number " + str(int(pocket)) + " is red.")
        else:
            print("  Pocket number " + str(int(pocket)) + " is black.")      #For this subset, even=red, odd=black


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()