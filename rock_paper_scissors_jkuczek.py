"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 03/05/2023

Description:
    This program utilizes three functions. The function "get_computer_choice" has the computer make a
    choice for the game. The function "get_player_choice" asks the user to make one of three choice,
    and if they make a choice ouside of the list, it reasks the user to make a choice. The function
    "get_winner" takes the computer and user choices as arguments and determines the outcome of the
    game. In the main, the user and computer makes a choice and the choices are printed. If the game
    is a tie, the game repeats. If the computer or user wins, it is stated. At the end, the program
    says thanks for playing.

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
def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return r.choice(options)                    #Computer makes choice

def get_player_choice():
    options = ["rock", "paper", "scissors"]
    h = input("Choose rock, paper, or scissors: ")              #Asks user for choice
    while h not in options:
        print("You made an invalid choice. Please try again.")
        h = input("Choose rock, paper, or scissors: ")          #Repeats if input not in list
    else:
        return str(h)                                           #Returns chouse

def get_winner(computer, player):
    if computer == "rock":
        if player == "rock":
            return "tie"
        elif player == "paper":
            return "player"
        else:
            return "computer"
    elif computer == "paper":
        if player == "rock":
            return "computer"
        elif player == "paper":
            return "tie"
        else:
            return "player"
    else:
        if player == "rock":
            return "player"
        elif player == "paper":
            return "computer"
        else:
            return "tie"        #Returns outcome of game

def main():
    p = get_player_choice()
    c = get_computer_choice()
    print(f"  The computer chose {c}, and you chose {p}.")      #Prints choices
    while get_winner(c, p) == "tie":
        print("  It's a tie. Starting over.\n")
        p = get_player_choice()
        c = get_computer_choice()                               #Repeats if tie
        print(f"  The computer chose {c}, and you chose {p}.")
    if get_winner(c, p) == "computer":
        print(f"  {c} beats {p}")
        print("  You lost.  Better luck next time.")            #Computer wins
    elif get_winner(c, p) == "player":
        print(f"  {p} beats {c}")
        print("  You won the game!")                            #User wins
    print("Thanks for playing.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
