"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 10.3 - COVID 19 Cases
Date: 04/07/2023

Description:
    The program reads a text file of COVID-19 data in Indiana and makes into a bar graph showing
    the total COVID-19 cases to date. The text file is opened and a list of each line is
    created. Then, a loop is used to convert the list of lines in a a list of each "term" in a
    line. The list is filtered into two lists, one for the start of the week dates, and the other
    for the new cases in each week. The elements in the new cases/week were converted to floats,
    and, for each element, itself and every element prior were summed, divided by 1000, and added
    to a new list. The dates were converted to a matplotlib friendly version of itself, and added
    to a new list. Then the bar graph was constructed, with the appropriate axis label, title, and
    bar widths. And, the plot is presented.

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
import matplotlib.pyplot as plt
import datetime

"""Write new functions below this line (starting with unit 4)."""


def main():
    l = []
    t = []
    start = []
    total = []
    with open("indiana_covid-19_data_spring_2023.txt") as c:
        for line in c:
            l.append(line.rstrip())     #List of lines in text file
    for lines in l:
        word = ''
        for ch in lines:
            if ch == ' ' and word != '':
                t.append(word)
                word = ''
            else:
                word += ch
        if word != '':
            t.append(word)              #Seperates 4 variables per line into 4 seperate strings
    start_dates = t[0::4]
    new_cases = t[2::4]                 #Filters out data that doesn't matter
    for i in new_cases:
        start.append(float(i))
    for i in range(0,len(start)):
        s = start[0:i+1]
        u = float(sum(s)/1000)
        total.append(u)                 #List of total COVID cases to date
    new_dates = []
    for date in start_dates:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        new_dates.append(dt)            #List of matplotlib friendly dates
    fig, ax = plt.subplots()
    ax.bar(new_dates, total,width=7)
    fig.autofmt_xdate()
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')
    plt.show()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
