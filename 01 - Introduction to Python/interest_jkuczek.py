"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 01.2 - Interest
Date: 01/22/2023

Description:
    The user inputs the principal, interest rate (in percent), the number of years of their investment, and
    the number of times interest is compunted. The porgram uses the compound interest equations to  output
    the future value of their inveestment (formated with commas and two decimal places) after their inputed
    number of years.

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
    print("Enter the following parameters.")                                                                            #Tells user to enter data
    P = int(input("  The initial deposit? "))                                                                           #Inputs principal
    r = float(input("  The annual interest rate in percent? "))                                                         #Inputs interest rate (percent)
    t = float(input("  The number of years the account earn interest? "))                                                 #Inputs time
    n = int(input("  The number of times interest is compounded each year: "))                                          #Inputs times interest compounded/year
    FV = P * (1 + (r/100)/n)**(n*t)                                                                                     #Compound interest equation for FV
    formatted_FV = "{:,.2f}".format(FV)                                                                                 #Formats FV for commas, two decimals
    formatted_t = "{:,.1f}".format(t)                                                                                   #Formats time for one decimal
    print("The balance of this account will be $" + str(formatted_FV) + " after " + str(formatted_t) + " years.")       #Ouputs FV


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
