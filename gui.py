from tkinter import END, Label,Frame,Button,StringVar,CENTER,Entry,Tk, Text
from func import *

#main
window = Tk()
window.geometry("400x500")

secretWord = getRandomWord()
guessCount = 6


#func
def raiseframe(frame):
    frame.tkraise()
    print("raised")

def submit(secretWord):
    usrInput = guessFieldVar.get()
    print(f"usrInput: {usrInput}")
    positions = checkGuess(usrInput,secretWord)
    print(positions)
    fragmentedGuess = list(usrInput)
    for i in range(len(fragmentedGuess)):
        if fragmentedGuess[i] in positions[0]:
            for j in range(len(positions[0])):
                allLetters[i-1][j] = fragmentedGuess[i]
                allLetters[i-1][j].configure(fg="green")
                #update colour of i letter here to green
        elif fragmentedGuess[i] in positions[1]:
            for j in range(len(positions[0])):
                allLetters[i-1][j] = fragmentedGuess[i]
                allLetters[i-1][j].configure(fg="orange")
                #update colour of i letter here to orange
        else:
            allLetters[i-1][j] = "*"
            allLetters[i-1][j].configure(fg="red")
            #update the remaining letters to * and set colour to red



mainFrame = Frame(window, bg="green")
mainFrame.place(x=0,y=0,width=400,height=500)
menuFrame = Frame(window, bg="light blue")
menuFrame.place(x=0,y=0,width=400,height=500)

#-----MAIN MENU OBJECTS -----
playButton = Button(menuFrame, text="Play", width=20, command=lambda:raiseframe(mainFrame)).place(x=100,y=100)
title = Label(menuFrame, text="Wordle").place(relx=.5, rely=.1,anchor=CENTER)

#-----MAIN FRAME OBJECTS -----
rowPosX = 32
rowPosY = 100
guesses = 6
width = 280
height = 43


r1 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.155,anchor=CENTER)
r1Vars = [StringVar() for i in range(5)]
r1Letters = [Label(r1, textvariable=r1Vars[i]) for i in range(5)]
r2 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.255,anchor=CENTER)
r2Vars = [StringVar() for i in range(5)]
r2Letters = [Label(r2, textvariable=r2Vars[i]) for i in range(5)]
r3 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.355,anchor=CENTER)
r3Vars = [StringVar() for i in range(5)]
r3Letters = [Label(r3, textvariable=r3Vars[i]) for i in range(5)]
r4 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.455,anchor=CENTER)
r4Vars = [StringVar() for i in range(5)]
r4Letters = [Label(r4, textvariable=r4Vars[i]) for i in range(5)]
r5 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.555,anchor=CENTER)
r5Vars = [StringVar() for i in range(5)]
r5Letters = [Label(r5, textvariable=r5Vars[i]) for i in range(5)]
r6 = Frame(mainFrame, borderwidth=2,relief="solid",width=width,height=height).place(relx=0.5,rely=0.655,anchor=CENTER)
r6Vars = [StringVar() for i in range(5)]
r6Letters = [Label(r6, textvariable=r5Vars[i]) for i in range(5)]

allLetters = [r1Letters,r2Letters,r3Letters,r4Letters,r5Letters,r6Letters]

guessFieldVar = StringVar()
guessField = Entry(mainFrame,textvariable=guessFieldVar).place(relx=0.5,rely=0.8,anchor=CENTER,width=170,height=50)
submitButton = Button(mainFrame, text="Submit",command=submit(secretWord)).place(x=290,rely=0.765)
#mainloop
window.mainloop()