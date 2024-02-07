from colorama import Fore
from func import *

secretWord = getRandomWord()
print(secretWord)

guesses=6

while guesses > 0:
    usrinp = str(input("Enter guess:"))
    if len(usrinp) == 5:

        positions = checkGuess(usrinp,secretWord)
        if usrinp == secretWord:
            print(f"you win! the word was {secretWord}")
            break
        else:
            fragmentedGuess = list(usrinp)
            fragmentedsecret = list(secretWord)
    else:
        print("invalid input")
