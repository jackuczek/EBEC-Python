"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 01.1 - Road Trip
Date: 01/18/2023

Description:
    This program provides the user with the cost of their car trip, given the distance of their trip,
    the price per gallon of gas, and the mpg of their vehicle.

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
def rounddown(n):           #Function so cost output in rounded down
    return(int(n//1))

def main():
    print("Road trip fuel cost estimator:")
    distance = float(input("  How far away is your destination (miles)? "))             #User inputs distance
    price = float(input("  What is the average price of gas (dollars per gallon)? "))   #User inputs price of gas
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))         #User inputs mpg
    cost = rounddown((2 * distance) * price/mpg)                                        #Equation for cost
    print("\nThe fuel cost for this trip is approximately $" + str(cost) + ".")         #Prints cost


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
