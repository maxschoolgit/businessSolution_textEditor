from tkinter import *
from tkmacosx import Button

def writeFile():
	with open("demofile.txt", "w") as f:
		f.write(typing_box.get("1.0",END))

def readFile():
	with open("demofile.txt", '')

#Creates window
root = Tk()
root.title("This Is The Greatest Text Editor Of All Time")
root.geometry("600x400")

#Buttons, text, etc.
file_button = Button(root, text="Save", command=writeFile)
fileload_button = Button(root, text="Load", command=readFile)
typing_box = Text(root, bg = 'light grey', fg = 'black', bd = 5, font = 'Times')


#Pack/Grid
file_button.pack()
fileload_button.pack()
typing_box.pack()

#GUI Event Loop
root.mainloop()