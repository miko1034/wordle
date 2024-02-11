from termcolor import colored
from tkinter import *
from func import *

#main
window = Tk()
window.geometry("400x500")

#func
def raiseframe(frame):
    frame.tkraise()
    print("raised")

def submit():
    usrInput = guessField.get(0.0,END)
    print(f"usrInput: {usrInput}")
    result = checkGuess()
    return result

mainFrame = Frame(window, bg="green")
mainFrame.place(x=0,y=0,width=400,height=500)
menuFrame = Frame(window, bg="light blue")
menuFrame.place(x=0,y=0,width=400,height=500)

#-----MAIN MENU OBJECTS -----
playButton = Button(menuFrame, text="Play", width=20, command=lambda:raiseframe(mainFrame)).place(x=100,y=100)
title = Label(menuFrame, text="Wordle").place(relx=.5, rely=.1,anchor=CENTER)

#-----MAIN FRAME OBJECTS -----
rows = [["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],
        ["","","","",""],]

rowPosX = 32
rowPosY = 100
guesses = 6

r1var = StringVar()
r2var = StringVar()
r3var = StringVar()
r4var = StringVar()
r5var = StringVar()
r6var = StringVar()
r1 = Label(mainFrame, textvariable=r1var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.155,anchor=CENTER)
r2 = Label(mainFrame, textvariable=r2var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.255,anchor=CENTER)
r3 = Label(mainFrame, textvariable=r3var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.355,anchor=CENTER)
r4 = Label(mainFrame, textvariable=r4var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.455,anchor=CENTER)
r5 = Label(mainFrame, textvariable=r5var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.555,anchor=CENTER)
r6 = Label(mainFrame, textvariable=r6var, borderwidth=2,relief="solid",width=48,height=2).place(relx=0.5,rely=0.655,anchor=CENTER)
for i in range(guesses):
    pass

guessField = Entry(mainFrame).place(relx=0.5,rely=0.8,anchor=CENTER,width=170,height=50)
submitButton = Button(mainFrame, text="Submit",command=lambda:submit).place(x=290,rely=0.765)
#mainloop
window.mainloop()