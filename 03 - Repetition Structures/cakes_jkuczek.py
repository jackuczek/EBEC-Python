"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 03.1 - Cakes
Date: 02/13/2023

Description:
    The program prints layer of asterisks surrounded by a bracked to appear as layers of a cake.
    The programs asks for user input on the number of layers. The whole program loops a number of
    times equal to the number of layers the user inputted. For each loop, the program prints
    a number of spaces equal to the number of layers minus which loops its on minus 1 for the layers
    to be centered, prints a [ bracket, prints a odd numbered of brackets approprate to the layer
    number, and prints a ] bracket. For every loop, the number of spaces goes down by one and
    the number of asterisks go up by 2.

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
    layers = int(input("Enter the number of layers: "))     #Asks for num. of layers

    for i in range(layers):                                 #Loops for number of layers
        for j in range(layers-i-1):
            print(" ",end="")                               #Prints spaces for centered layers
        print("[", end="")
        for j in range(2*i+1):
            print("*",end="")                               #Prints * in series of increasing odd numbers
        print("]")
            


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
