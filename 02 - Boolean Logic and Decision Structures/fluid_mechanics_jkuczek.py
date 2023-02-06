"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 02/05/2023

Description:
    The program asks the user to input a temperature (either 5, 20, or 50 degrees C), a velocity (in m/s), and a diamter (in m). The programs chooses the
    corresoponding kinematic viscosity depending on the temperature. The programs then uses the temperature, velocity, and kinematic viscosity to
    calculate the Reynold's number. The program then formats the calculated Reynold's number in scientific notation, and then prints an appropriate output
    to the user repeating their inputs and the formatted Reynold's number.

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
    T = float(input("Enter the temperature in °C as 5, 20, or 50: "))
    V = float(input("Enter the velocity of water in the pipe (m/s): "))
    D = float(input("Enter the pipe's diameter (m): "))                         #User inputs infor
    if T == 5:
        KV = .00000152
    elif T == 20:
        KV = .000001
    else:
        KV = .000000554                                                         #Chooses corresponding FV
    RE = (V*D)/KV                                                               #Equation
    format_RE = "{:.2e}".format(RE)                                             #Formats to scientific notation with two decimal places
    print("At " + str(T) + "°C, the Reynolds number for flow at " + str(V) + " m/s in a " + str(D) + " m diameter pipe is " + str(format_RE) + ".")   #Output


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
