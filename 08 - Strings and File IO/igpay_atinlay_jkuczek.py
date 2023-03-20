"""
Author: Jacob Kuczek, jkuczek@purdue.edu
Assignment: 08.1 - Igpay Atinlay
Date: 03/19/2023

Description:
    The program uses the function "igpay" to translate a user inputed sentence in Pig Latin into
    English. The function "igpay" takes a the user inputed sentence as an argument. The sentence
    is split into a list of individual words, and, for every word, the "ay" is removed and the last
    letter is put to the front. The new word is added to a list of translated words. The list of
    translated words are joined back together into a sentence and only the first letter is
    capitalized. The new sentence is returned. In the main, it asks the user for a sentence in
    Pig Latin, the function is translated, and the translation is printed.

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
def igpay(pig_latin):
    word_list = pig_latin.split()                   #Splits sentence into list of individual words
    new_words = []
    for word in word_list:
        word = word.replace("ay","")
        new_word = word[-1] + word[0:len(word)-1]
        new_words.append(new_word)                  #For every word, takes out "ay" and puts last letter in front
    translation = " ".join(new_words)
    translation = translation.capitalize()          #Joins words and capitalizes only first letter
    return translation


def main():
    sentence = str(input("Enter a string in Pig Latin: "))  #User input sentence as string
    translation = igpay(sentence)                           #Calls function
    print(f"Translation: {translation}")                    #Prints translation


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
