"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 03/17/2023

Description:
    The program creates two functions - roll_d6 and get_2d6_rolls - to create a table that shows the
    user the proportion of each possible sum of two d6 die 2-12 is in the list of 1 million
    occurances of the sum of 2 d6 die as a percentage. The roll_d6 function uses the random module
    to choose a number between 1 and 6. The get_2d6_rolls takes the number of rolls as an argument
    and forms a list of the sum of rolling the two die using the roll_d6 function. The length of the
    list is equal to the argument. In the main, It uses the get_2d6_rolls function to roll 2d6 1
    million times, and forms a table of the percentages which each sum has occured.

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
def roll_d6():
    return r.randrange(1,7)         #Function "rolls" d6

def get_2d6_rolls(repeats):
    sums = []
    for i in range(repeats):
        x = roll_d6()
        y = roll_d6()
        sums.append(x+y)
    return sums                     #Functions rolls two dice and puts sum into list

def main():
    l = get_2d6_rolls(1000000)      #List of sums of rolling 2 d6 1 million tims
    print("Roll  Frequency")
    for i in range(2,13):
        print(f"{i:>3}    {l.count(i)/len(l)*100:>5.2f}%")  #Creats formatted table of percentage of occurance of num 2-12
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
