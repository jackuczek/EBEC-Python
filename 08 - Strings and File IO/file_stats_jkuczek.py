"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.3 - File Stats
Date: 03/25/2023

Description:
    The program provides the user with the number of words, number of lines, and average words per
    line of a text file. The program establishes an empty list and sets the initial number of words
    as 0. The program opens the text file, and, for each line, adds the line with the trailing ends
    striped to the empty list. Then, for each line in the list, the line is split into a strin and the
    number of words is added to the original total. There is then a loop that, for each line in the
    list of lines, any blank line is removed. Then, the program prints the data about the text file.

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
    number_of_words = 0
    with open("frontiero_v_richardson.txt") as t:
        for line in t:
            l.append(line.rstrip())                #Creates string of each line as element
        for line in l:
            lines = line.split()
            number_of_words += len(lines)    #Counts number of words for each line
    for element in l:
        if element == "":
            l.remove(element)
        else:
            pass                #Removes blank lines
    number_of_lines = len(l)    #Num of lines in length of list of lines
    print(f"Total number of words: {number_of_words}")
    print(f"Total number of lines: {number_of_lines}")
    print(f"Average number of words per line: {number_of_words/number_of_lines:.1f}")   #Prints data


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
