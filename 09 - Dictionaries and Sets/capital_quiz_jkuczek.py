"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 04/02/2023

Description:
    The program constructs a state and their capital quiz for the user to take. The program has a
    function called "gat_state_data" that opens the txt file of every state and their capital and
    contructs a dictionary with the state as the key and the capital as the value. In the main,
    the function is called to provide the list, and a list of states is postulated and shuffled.
    While there are elements in states, the program asks the user for the for the capital of a given
    state. If its correct, it tells the user they are correct and removes the item from the list so
    it can't be asked again. If its wrong, it tells them they are wrong, provides the correct answer,
    and is not removed so that, once the user has a chance to answer the initial 50 questions, the
    questions they got wrong are asked again. If the user enters a "0," the quiz ends, telling the
    user they didn't answer any questions if no questions are answered, or their score if more than
    1 questions was answered.

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
def get_state_data():
    d = {}
    with open('state_capitals.txt') as c:
        for line in c:
            string = line.split(",")
            old = string[1]
            key = old[:-1].lstrip()
            value = string[0]
            d[key] = value              #Creates dictionary for states and capitals
    return d

def main():
    correct = 0
    total = 0
    exit = False
    questions = get_state_data()
    states = list(questions.keys())
    r.shuffle(states)                   #Randomizes order
    i = 0
    while states:
        i = 0
        if exit == True:
            break
        state = states[i]
        capital = questions[state]
        answer = input(f"What is the capital of {state} (enter 0 to quit)? ").title()   #User inputs their answer
        if answer == "0":
            exit = True
            break               #Ends quiz if "0"
        elif answer == capital:
            print("  That is correct!")
            correct += 1 
            total += 1
            states.remove(state)        #Removes state if correct
        else:
            print("  That is incorrect.")
            print(f"  The capital of {state}"+f" is {capital}.")
            total += 1          #Keeps state in list if wrong
        i += 1
    if total == 0:
        print("You didn't answer any questions.")   #Says no questions answered if 0 questions answered
    else:
        print(f"You answered {correct/total*100:.1f}% of the questions correctly.") #Provides score if answered >0 questions



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
