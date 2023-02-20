"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 04.5 - Prime List
Date: 02/19/2023

Description:
    The program defined the function "is prime", which says that an argument "integer" is False
    if its 1, True if its 2, and then a loop which divides the inputted value by every number
    between 2 and itself minus 1, and if its ever divisible, then its True, and False otherwise.
    This is done by returning Boolean expressions.. In the main, a list is estbalished for the
    sequence of prime numbers between 2 and the inputted number. The program asks for user input. The
    program goes through every number between 2 and the inputted number, and, if the number is prime,
    it is added to the list, and, if it is not prime, nothing happens. After the loop, the list of
    primes are printed.

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
def is_prime(integer):
    if integer == 1 or integer == 0:                    #Not prime if 1 or 0
        return False
    elif integer == 2:
        return True                                     #Prime if 2
    elif integer > 2:
        for i in range(2,int(integer**(1/2))+1):
            if (integer%i) == 0:
                return False                            #Prime if divisible by number between 1 and itself-1
    return True                                         #Not prime otherwise


def main():
    list = []
    i = int(input("Enter a positive integer: "))
    for j in range(2,i+1):                              #Loops from 2 to i
        if is_prime(j) == True:
            list.append(j)                              #If num is prime, added to list
        else:
            pass                                        #If num not prime, nothing happens
    print(f"The primes up to {str(i)} are: ",end="")
    print(*list, sep = ', ')                            #Prints list with commas


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
