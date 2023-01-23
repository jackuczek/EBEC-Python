"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 01/23/2023

Description:
    The program asks the user the number of cookies they want to make. The program then calculates the
    necessary number of cups of butter, sugar, and flour the user needs to make the specified number of
    cookies based on a recipe for 48 cookies. The program also formats the numerical outputs to have
    commas, necessary decimal places, and width 10.

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
    cookies = float(input("How many cookies do you want to make? "))            #Asks user number of cookies
    butter = cookies * 1.25/48
    sugar = cookies * 1.5/48
    flour = cookies * 2.5/48                                                    #Calculates amount of butter, sugar, and flour
    formatted_cookies = "{:,.0f}".format(cookies)                               #Formats cookies to have commas and no decimals
    formatted_butter = format(butter, '10,.2f')
    formatted_sugar = format(sugar, '10,.2f')
    formatted_flour = format(flour, '10,.2f')                                   #Formats butter, sugat, and flour to have commas and two decimals
    print("To make " + str(formatted_cookies) + " cookies, you will need:")
    print(str(formatted_butter) + " cups of butter")
    print(str(formatted_sugar) + " cups of sugar")
    print(str(formatted_flour) + " cups of flour")                   #Outputs amount of sugar, butter, and flour in cups


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
