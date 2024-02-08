#from colorama import Fore
from func import *

secretWord = getRandomWord()
print(secretWord)

guesses=6
to_print = ""

while guesses > 0:
    usrinp = str(input("Enter guess:"))
    if len(usrinp) == 5:
        if usrinp == secretWord:
            print(f"you win! the word was {secretWord}")
            break
        else:
            positions = checkGuess(usrinp,secretWord)
            print(positions)
            fragmentedGuess = list(usrinp)
            fragmentedsecret = list(secretWord)   # [[4],[1],[0,3,2]]  <-- How guess is returned after check
            for i in range(len(positions[1])):
                yellowIndexes = fragmentedsecret.index(positions[1][i])
            for i in range(len(positions[0])):
                greenIndexes = fragmentedsecret.index(positions[0][i])    
            for i in range(5):
                if i != yellowIndexes or greenIndexes:
                    reconstructedWord =+ "*"
                else:
                    if i # no workie



                #get indexes of all yellows
                #get indexes of all greens
                #add gray letters to list of bad chars
                #fill in the unguessed letters in the user guess with *
            
            guesses = guesses - 1
            print(f"you have {guesses} left")
    else:
        print("invalid input")
