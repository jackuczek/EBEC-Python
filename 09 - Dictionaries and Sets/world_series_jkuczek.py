"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 09.2 - World Series
Date: 04/02/2023

Description:
    This program provides the user statistic about the World Series winner in a year and the number
    of time the team won the World Series. The function "load_winners_data" uses the txt file with a
    list of World Series winners, and creates a list of winners. The first loop establishes the
    dictionary with key being the year and value being the winning team. The second loop establishes
    the dictionary with key team name and value number of times they have won the World Series. The
    dictionaries are returned. The main function gets the two dictionaries from the function. The
    user inputs a year. If the year is before the World Series began or in the future, then it says
    its not in the system. If the year inputted is one of the two years the World Series didn't
    happen, it tells the user it didn't happen. Otherwise, it tells the user the winner and how many
    times they have won it till 2022.

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
def load_winners_data():
    l = []
    d1 = {}
    d2 = {}
    with open("WorldSeriesWinners.txt") as w:
        for line in w:
            l.append(line.rstrip())             #List of teams
    i = 1902
    for team in l:
        if i == 1903 or i == 1993:
            i += 1
        i += 1
        d2[i] = team                            #Creates dictionary pairing year and winner
    for team in l:
        value = team.rstrip()
        if value in d1.keys():
            d1[value] += 1
        else:
            d1[value] = 1                       #Creates dictionary pairing team and # of times won
    return d1, d2

def main():
    d1, d2 = load_winners_data()
    year = int(input("Enter a year in the range 1903 -- 2022: "))   #User inputs year
    if year < 1903 or year > 2022:
        print(f"  Data for the year {year} is not included in this system.")    #Not included if before world series conception or didn't happen yet
    elif year == 1904 or year == 1994:
        print(f"  The World Series wasn't played in the year {year}.")          #World series not played
    else:
        print(f"  The {d2[year]} won the World Series in {year}.")
        print(f"  They have won the World Series {d1[d2[year]]} times.")        #Stats if world series happened in year


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
