"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/01/2023

Description:
    The program asks the user to input the number of packages that will be purchased. If they input a number less than 0, it will say that is an invalid input.
    If the number of packages is from 0 to 3, then it says there is no discount and outputs the price. If the number of packages is greater than or equal to
    4, then the program tells the user the appropraite discount given the quantity, calculates and formats the new price, and tells the user the price of
    their order depending on the quantity of packages.

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
    quantity = float(input("How many packages will be purchased: "))                                                #Asks for quantity
    if quantity < 0:
        print("  Invalid Input!")
    elif 0 <= quantity <= 3:                                                                                        #Invalid input if less than 0 packages
        print("  No discount applied.")
        discount = quantity * 880
        discount = "{:,.2f}".format(discount)
    elif 4 <= quantity <= 39:
        print("  10% discount applied.")
        discount = quantity * 880 * 0.9
        discount = "{:,.2f}".format(discount)
    elif 40 <= quantity <= 199:
        print("  15% discount applied.")
        discount = quantity * 880 * 0.85
        discount = "{:,.2f}".format(discount)
    elif 200 <= quantity <= 999:
        print("  30% discount applied.")
        discount = quantity * 880 * 0.7
        discount = "{:,.2f}".format(discount)
    elif quantity >= 1000:
        print("  42% discount applied.")
        discount = quantity * 880 * 0.58
        discount = "{:,.2f}".format(discount)                                                                       #Calculates and formats price depending on quantity
    if quantity >= 0:
        print("  The total price to purchase " + str(int(quantity)) + " packages is $" + str(discount) + ".")       #Outputs price and quantity
    else:
        pass                                                                                                        #Says nothing if less than 0 packages


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
