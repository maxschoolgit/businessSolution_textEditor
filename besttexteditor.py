from tkinter import *
from tkmacosx import Button

#Creates window
root = Tk()
root.title("This Is The Greatest Text Editor Of All Time")
root.geometry("600x500")

#Buttons, text, etc.
file_button = Button(root, text="File")
typing_box = Text(root, bg = 'light grey', fg = 'black', bd = 5, font = 'Times')


#Pack/Grid
file_button.pack()
typing_box.pack()

#GUI Event Loop
root.mainloop()