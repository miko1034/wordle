from termcolor import colored
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
            output = []
            for i in range(len(fragmentedGuess)):
                if fragmentedGuess[i] in positions[0]:
                    output.append(colored(f"{fragmentedGuess[i]}", "green"))
                elif fragmentedGuess[i] in positions[1]:
                    output.append(colored(f"{fragmentedGuess[i]}", "yellow"))
                else:
                    output.append(colored("*", 'light_grey'))
            output = "".join(output)
            print(output)
    else:
        print("invalid input")

#ok partially works. kinda broken when word is (for example) "risky" and you guess risks
#then it kinda breaks... but we move
