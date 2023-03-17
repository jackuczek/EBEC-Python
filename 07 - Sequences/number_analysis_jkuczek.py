"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 03/16/2023

Description:
    The program uses the function "get_number_list" to get 10 numbers for a user and outputs the
    maximum, minimumum, total, and mean of the list of numbers. The function "get_number_list"
    uses a loop for asks the user for numbers 1 through 10, and returns the list l of the user-
    inputted numbers. In the main portion, the function is called, and number analysis is done and
    printed for the maximum, minimumum, total, and mean of the list of numbers l.

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
def get_number_list():
    l = []
    for i in range(1,10+1):
        l.append(float(input(f"  number {i:>2} of 10: ")))  #Loop that asks for num i/10 and adds to list
    return l                                                #Returns list


def main():
    print("Enter 10 numbers:")
    l = get_number_list()                                   #Uses function to get list of 10 num
    print(f"Highest number: {max(l):.2f}")
    print(f"Lowest number: {min(l):.2f}")
    print(f"Total: {sum(l):.2f}")
    print(f"Average: {sum(l)/len(l):.2f}")                  #Finds max, min, sum, and avg of numbers in list



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
