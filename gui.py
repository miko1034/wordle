from tkinter import *
from func import *

#main
window = Tk()
window.geometry("400x500")

#func
def raiseframe(frame):
    frame.tkraise()
    print("raised")

def guess():
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
rows = [[],[],[],[],[],[]]

guessField = Entry(mainFrame).place(relx=0.5,rely=0.6,anchor=CENTER,width=170,height=50)
submitButton = Button(mainFrame, text="Submit",command=lambda:guess).place(x=300,rely=0.565)
#mainloop
window.mainloop()