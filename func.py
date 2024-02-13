import random

def getRandomWord():
    with open("wordlist.txt", "r") as f:
        wordlist = f.readlines()
    #cleans the list
    for i in range(len(wordlist)):
        wordlist[i]=wordlist[i].strip()
    return wordlist[random.randint(0,len(wordlist)-1)]


def checkGuess(userInput, chosenWord):
    gray = []
    yellow = []
    green =[]
    for i in range(5):
        if userInput[i] == chosenWord[i]:
            green.append(userInput[i])
        elif userInput[i] in chosenWord:
            yellow.append(userInput[i])
        else:
            gray.append(userInput[i])
    return [green,yellow,gray]


