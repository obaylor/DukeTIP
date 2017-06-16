from __future__ import print_function
import numpy


# Print Hangman's current state
def printHangman(numberWrong):
    # Print the hangman
    print("  |------|")
    if numberWrong >= 1:
        print("  |      0")
    else:
        print("  |")
    if numberWrong >= 2:
        print("  |      |")
    else:
        print("  |")
    if numberWrong >= 3:
        print("  |     /|\\")
    else:
        print("  |")
    if numberWrong >= 4:
        print("  |      |")
    else:
        print("  |")
    if numberWrong == 5:  # can't be > here so we get to the else :)
        print("  |     /")
    elif numberWrong >= 6:
        print("  |     / \\")
    else:
        print("  |")# don't print any legs
        print("-----")# print bottom of noose

def printBlanks(word, correctLetters):
    solved = True# Set solved equal to true (innocent until proven guilty)
    # Loop over each letter in the word
    for l in word:
        l = l.lower()  # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctLetters:  # Remove "False" and replace it with the appropriate condition
            print(l + " ", end = "")# If it is, print the letter and a space
        else:
            # If it isn't, print an underscore and a space
            print ("_ ",end = "")
            solved = False# Also, set solved equal to False
    print()
    print()
    return solved

word_list = ["test", "something", "it"]# Define a list of words as options


correctLetters = [ ]# Define a list to hold the correctly guessed letters

incorrectGuesses = 0# Define a variable to count the number of incorrect guesses


word = numpy.random.choice(word_list)# Pick a random word to be used

# Repeat forever, we'll use a break to get out
while True:
    # Print the Status of the Hangman
    printHangman(incorrectGuesses)
    # Print the word blanks and see if they solved it
    solved = printBlanks(word, correctLetters)  # Replace False with a function call

    if incorrectGuesses >= 6:
        print ("You Lose")# Catch Death (Exit loop if they got 6 or more wrong)
        break

    if solved:
        print('You win!')
        break  # no need to guess again

    user_input = ""
    while len(user_input) != 1:
        user_input = raw_input("Please enter a letter")# Define a variable to hold user input
    # Loop until they give a letter

    # Check if the letter is in the word
    if user_input in word:  # Replace True with the correct condition
        correctLetters.append(user_input)# If it's right, put it in the correct letters list and let them know it was right
    else:
        incorrectGuesses = incorrectGuesses + 1# If it's wrong, increment the wrong count and let them know it was wrong
    print()

print ("The word was " + word)# Reveal what the word was