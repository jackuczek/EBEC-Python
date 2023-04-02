"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 09.3 - Course Info
Date: 04/02/2023

Description:
    This program provides the instructor, room number, and time of a specified course using the
    function "get_course_data." The function constructs the nested dictionary with the course
    number as keys and a dictionary of associated info as the value. In the main, the nested
    dictionary is retrieved and the user inputs a course number. If the course is not in the
    dictionary, the program says the course number is invalid. If it does exist, the value for the
    associated course number/key is retreived. Then, for every pair of key and value there is in the
    course infor dictionary, it is printed and aligned so the formatting is appealing.

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
def get_course_data():
    course_data = {"CS101":{"instructor":"Django", "room":"1461", "time":"9:00 a.m."},
                   "CS102":{"instructor":"Idle", "room":"4815", "time":"11:00 a.m."},
                   "CS103":{"instructor":"Rich", "room":"3634", "time":"10:00 a.m."},
                   "NT110":{"instructor":"Marshal", "room":"1188", "time":"2:00 p.m."},
                   "CM241":{"instructor":"Pickle", "room":"2451", "time":"12:00 p.m."}} #Course data in nested dictionary
    return course_data


def main():
    course_data = get_course_data()
    key = str(input("Enter a course number: "))         #User inputs course #
    if key in course_data:
        course_info = course_data.get(key)              #Retrives list dictionary associated with course#
        print(f"  The details for course {key} are:")
        for k,v in sorted(course_info.items()):
            print(f"{k.capitalize():>14}: {v}")         #Loops printing of course info.
    else:
        print(f"  {key} is an invalid course number.")  #Invalid if course # DNE


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
