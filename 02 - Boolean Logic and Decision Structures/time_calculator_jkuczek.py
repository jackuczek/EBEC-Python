"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 02/05/2023

Description:
    This program asks the use to input a number of seconds. The program then calculates how many days,
    hours, minutes, and remaining seconds the inputed number of seconds is equivalent to. If the inputed
    number of seconds is less than 60, then it says its less than a minute. If it's more than 60, then
    the program does calculations for number of days, hours, minutes, and remaining seconds, and,
    depending on whether or not those values are 0, they are correctly categorized so the appropriate
    response is constructed.

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
    time = int(input("Please enter a time in seconds: "))           #User inputs time
    if time < 60:
        print(f"  {time:,} seconds is less than one minute.")
        return()                                                      #If <60, less than minute
    d = time // 86400
    h = time % 86400 // 3600
    m = time % 3600 // 60
    s = time % 60                                                   #Time calculations
    print(f"  {time:,} " + "seconds equals ", end = '')
    strdays = (f"{d} day(s)")
    strhours = (f"{h} hour(s)")
    strminutes = (f"{m} minute(s)")
    strseconds = (f"{s} second(s)")                                 #Appropriate strings
    if 60 <= time < 3600:
        print(strminutes, end = "")
        if s != 0:
            print(" and " + strseconds, end = "")
        print(".")
    elif 3600 <= time < 86400:
        print(strhours, end = "")
        if m and s != 0:
            print(", ", end = "")
        elif m ^ s != 0:
            print(" and ", end = "")
        if m != 0 and s == 0:
            print(strminutes, end = "")
        elif m and s != 0:
            print(strminutes + " and ", end = "")
        if s != 0:
            print (strseconds, end = "")
        print(".")
    elif time >= 86400:
        print(strdays, end = "")
        if h != 0:
            if m == 0 and s == 0:
                print(" and " + strhours, end = "")
            else:
                print(", " + strhours, end = "")
        if m and s != 0:
            print(", ", end = "")
        elif m ^ s != 0:
            print(" and ", end = "")
        if m != 0 and s == 0:
            print(strminutes, end = "")
        elif m and s != 0:
            print(strminutes + " and ", end = "")
        if s != 0:
            print(strseconds, end = "")
        print(".")                                                  #Categorizations of responses




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
