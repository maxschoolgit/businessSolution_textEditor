from tkinter import *
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("Writing Files")

#Set size of window
root.geometry("300x150")

#Commands
def writeFile():
	with open("demofile.txt", "w") as f:
		f.write("This is what will be inside of the file!")
	print("You entered" + text)


#Button+Text Box
writebutton = Button(root, text='Write!', command=writeFile)
textbox = Text(root, height = 5, width = 32)
text = textbox.get("1.0", END)



#Pack+Run
writebutton.pack()
textbox.pack()
root.mainloop()
