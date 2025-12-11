from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Red Light, Green Light")

#Set size of window
root.geometry("500x400")

# Create buttons/text
text = Text(root, bg = 'grey', fg = 'black', bd = 5, font = 'Times')
red_button = Button(root, text="Red", background='red')
green_button = Button(root, text='Green', background='green')
yellow_button = Button(root, text='Yellow', background='yellow')
above_label = Label(root, text='This is a stoplight')

#Add a label
label = Label(root, text="Red Light, Green Light!")

# Place widgets in window (with pack function!)
label.pack()
red_button.pack()
green_button.pack()
yellow_button.pack()
above_label.pack()
text.pack()


# Start the GUI event loop
root.mainloop()
