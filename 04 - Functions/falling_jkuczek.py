"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 04.1 - Falling
Date: 02/18/2023

Description:
    The program defines the function "falling_dist" that takes x as a parameter and returns a calculation for the distance the object falls given a time t. Before
    the loop, the first time is defined as 5 and the header of the table and the lists are established. In the loop, it appends the time to the t list, r is
    defined as the output of "falling_dist" and is formatted and appened to list d, and the time goes up by 5. The loop continues until the time is equal to 50.
    After the loop, the two lists are printed into columns to complete the table.

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
def falling_dist(x):
    return .5*8.87*x**2                       #Function the does calculation

def main():
    time = 5
    print("Time (s)  Distance (m)\n----------------------")
    t = []
    d = []                                  #Establishes lists
    while time <= 50:
        t.append(int(time))
        r = falling_dist(time)
        r = "{:.1f}".format(r)
        d.append(str(r))                    #Uses function to do calculation and append to list
        time += 5
    for j in range(0,len(t)):
        print(f"{t[j]:>8}   {d[j]:>11}")    #Makes table




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
