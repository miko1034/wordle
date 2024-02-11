from tkinter import*
#from func import *

#rword = getRandomWord()
#print(rword)

#a = checkGuess("house",rword)
#print(a)

rows = [["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],]

def rowWrite(rows):
    guesses = 6
    for i in range(guesses):
        word = str(input("enter word: "))
        split = list(word)
        for j in range(5):
            rows[i][j] = split[j]
        print(rows)
    return rows

rowWrite(rows)

