"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 02/18/2023

Description:
    The program establishes the function "lucky_sum" that creates a list called s for the numbers to
    be placed into. There are two paths is the first number is larger than the second and if the
    second is larger than the first, so arguments can be given in either order. The paths do the
    same thing, which is not put the number in the list if it is divisible by 3, and does otherwise.
    The function returns the ultimate sum of all the numbers in the list. In the main, it asks the
    user to input the endpoits, uses user input as arguments of the function, and outputs and
    formats the sum.

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
def lucky_sum(first, second):
    s = []                          #Begins list
    if first < second:
        while first <= second:
            if first % 3 == 0:
                pass
            else:
                s.append(first)
            first += 1              #Puts all num not div. by 3 if first < second into list
    else:
        while first >= second:
            if second % 3 == 0:
                pass
            else:
                s.append(second)
            second += 1             #Puts all num not div. by 3 otherwise into list
    return sum(s)                   #Returns sum of num. in list

def main():
    f = int(input("Enter the first integer: "))
    s = int(input("Enter the second integer: "))            #Intput endpoint integers
    r = lucky_sum(f,s)                                      #Uses functions
    print(f'The sum of the lucky numbers is {int(r):,}.')   #Prints and formats output
    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
