"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.5 - Number Reader
Date: 03/26/2023

Description:
    The program provides the stats of the numbers in a text file. The program first opens the txt
    file and goes line by line, transfering the numbers into a list as an int and removing any loose
    ends. The list is then sorted so that the numbers are sequenetial. Then, the program provides
    the number of numbers in the txt file as the length of the list, the minimum number as the first
    number in the sequential list, the maximum number as the last number in the list, the sum of all
    numbers, and the average number by dividing the sum by the length. The outputs are formatted
    appropriately.

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
    l = []
    with open("random_numbers.txt") as r:
        for line in r:
            l.append(int(line.rstrip()))        #Converts numbers in txt into list of numbers
    l.sort()                                    #Sorts numbers in list sequentially
    print(f"{len(l):,} numbers were read from the file.")   #Total amount of numbers 
    print(f"Min: {l[0]:,}")         #1st number sequentially
    print(f"Max: {l[-1]:,}")        #Last number sequentially
    print(f"Sum: {sum(l):,}")       #Sum of all numbers
    print(f"Avg: {sum(l)/len(l):,.1f}")     #Avg number in list


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
