"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 03/05/2023

Description:
    This program defines a function called "random_factor" that takes the number of digits as an
    argument, and, using that argument and powers of tens, returns a random integers that has the
    given number of digits. The program defines a and b as 2 digit random int and 1 digit random int,
    respectively, and calculates c, the numerator. The program prints out the math questions to the
    user and formats it so its aligned, and asks the user for an answer. If the answer is equal to
    a, the 2 digit int, it tells the user they are right. Else, it says its wrong and tells the user
    the correct answer.

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
import random as r


"""Write new functions below this line (starting with unit 4)."""
def random_factor(digits):
    start = 10**(digits-1)
    end = (10**digits)-1                #Function takes # of digits and sets range using powers of 10
    return r.randint(start, end)


def main():
    a = random_factor(2)
    b = random_factor(1)                #Random 2 and 1 digit numbers
    c = a * b                           #Calculates numerators
    print(f"{c:>4}")
    print(f"\u00F7{b:>3}")              #Aligns numerator and denominator
    print("----")
    answer = int(input("= "))           #Asks for user answer
    if answer == a:
        print("Great job, that's correct!")
    else:
        print(f"Sorry, the correct answer is {a}.")          #If/else to tell user if they put right or wrong answer


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
