from tkinter import *
from tkmacosx import Button

#Heavy W.I.P.

#Creates window
root = Tk()
root.title("Updating Labels")
root.geometry("600x400")

#define function
def changeTitle():
	root.title(T.get("1.0",END))

#Create button
red_button = Button(root, text='change title!', command=changeTitle)
T = Text(root, height = 5, width = 32)

#pack
red_button.pack()
T.pack()

root.mainloop()
