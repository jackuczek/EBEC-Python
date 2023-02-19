"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 02/19/2023

Description:
    The program has 3 functions. The function "gat_valid_score" asks the user to enter a score. If
    the score is less than 0 or greater than 100, it tells the user the score is invalid and reasks.
    If it is valid, it returns the score that was inputted. The "calc_average" function takes a
    list of scores as an input, and returns the average score by dividing the sum of the scores by
    the number of scores. The "determine_grade" function determines the letter grade given a
    number score as an argument. In the main, the count starts at 0 and a list of scores s is
    established. A loop is done 5 times, where the score is the get_valid_score function, it prints
    the corresponding letter grade using the determine_grade function, adds the score to the list,
    and increases the count by 1. After the loop, the results are printed, where the average grade
    number and average letter grade are given using the calc_average and determine_grade functions.

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
def get_valid_score():
    score = float(input("Enter a score: "))             #Input for score
    while score < 0 or score > 100:
        print("  Invalid Input. Please try again.")
        score = eval(input("Enter a score: "))          #Reasks if score impossible
    else:
        return float(score)                             #Returns score

def calc_average(list):
    avg = sum(list)/len(list)
    return avg                                          #Calculates and returns avg

def determine_grade(grade):
    if 92 <= grade <= 100:
        return "A"
    elif 82 <= grade < 92:
        return "B"
    elif 73 <= grade < 82:
        return "C"
    elif 64 <= grade < 73:
        return "D"
    else:
        return "F"                                      #Determines letter grade


def main():
    count = 0
    grades = []                                         #List for grades
    while count <= 4:
        score = get_valid_score()
        print(f"  The letter grade for {score:.1f} is {str(determine_grade(score))}.")
        grades.append(score)
        count += 1                                                                       #Loops asking grade and outputing corresponding letter grade
    print("\nResults:")
    print(f"  The average score is {float(calc_average(grades)):.2f}.")
    print(f"  The letter grade for {float(calc_average(grades)):.2f} is {str(determine_grade(calc_average(grades)))}.")     #Uses functions to print avg. score and its letter grade





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
