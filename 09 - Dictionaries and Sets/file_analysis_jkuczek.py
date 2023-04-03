"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 09.4 - File Analysis
Date: 04/03/2023

Description:
    Attempted but was not able to figure it out.

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
    words_in_one = []
    words_in_two = []       #Words in txt files
    d1 = {}
    d2 = {}
    with open("python_1.txt") as a:
        for line in a:
            l = line.rstrip().split()
            for word in l:
                w = word.split
                w = word.lower()
                words_in_one.append(w + "\n")       #Attempt are making list of words w/out punctuation
    with open("python_2.txt") as b:
        for line in b:
            words_in_two.append(line.rstrip().lower())
    for word in words_in_one:
        value = word
        if value in d1.keys():
            d1[value] += 1
        else:
            d1[value] = 1                       #Dictionary for number of each word
    words_in_one = sorted(words_in_one)
    times_one = list(d1.values())
    with open("python_1_word_frequency.txt", "w") as word_one:
        word_one.writelines(words_in_one)           #Write text file of words


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
