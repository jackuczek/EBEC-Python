"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 07.4 - Magic Square
Date: 03/17/2023

Description:
    The program uses the functions "print_square" and "is_magic" to print each square under scrutiny,
    check if it is a Lu Shu magic square or not, and tells the user whether it is or not. The 
    "print_square" function uses a for loop to print the square and make it look nice and neat. The
    "is_magic" function checks assumes the square is a Lu Shu magic square, but says its not if it
    doesn't pass one of the horizontal, vertical, diagonal, and nonrepeating rules. In the main, a
    list is created of the three given squares, and uses a loop that prints each square, checks it,
    and tells the user whether it is a magic square or not.

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
def print_square(square):
    s = square
    for r in range(3):
        print("  ", end="")
        for c in range(3):
            q = s[r][c]
            if( (r == 0 and c == 2) or (r == 1 and c == 2)  or (r == 2 and c == 2)):
                index = print(f"{q}", end = '')
            else:
                index = print(f"{q} ", end = '')
        print("")
    return index            #Prints square so looks nice

def is_magic(square):
    check = True            #Assume True unles proven otherwise
    s = square
    if s[0][0]+s[0][1]+s[0][2] != 15 or s[1][0]+s[1][1]+s[1][2] != 15 or s[2][0]+s[2][1]+s[2][2] != 15:
        check = False       #Checks horizontal
    if s[0][0]+s[1][0]+s[2][0] != 15 or s[0][1]+s[1][1]+s[2][1] != 15 or s[0][2]+s[1][2]+s[2][2] != 15:
        check = False       #Checks vertical
    if s[0][0]+s[1][1]+s[2][2] != 15 or s[2][0]+s[1][1]+s[0][2] != 15:
        check = False       #Checks diagoncal
    flattenList = sum(s,[])
    for i in range (1,9):
        occurances = flattenList.count(i) 
        if(occurances > 1): #Checks for no repeats
            check = False
    return check    

def main():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    c = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    l = [a,b,c]                                         #List of given squares
    for i in l:
        print("Your square is:")
        print_square(i)
        if is_magic(i) == False:
            print("It is not a Lo Shu magic square.")
        else:
            print("It is a Lo Shu magic square!")       #Loops printing each square and checking
        if i == l[-1]:
            pass
        else:
            print("")                                   #Ensures space under check appears on every except last



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
