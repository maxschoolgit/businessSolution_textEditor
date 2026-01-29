from tkinter import *
from tkmacosx import Button
import random

#Heavy W.I.P.



#Creates window
root = Tk()
root.title("Updating Labels")
root.geometry("600x400")

#define function
def ButtonUpdate1():
	one_label.config(text = "Updated 1")


def ButtonUpdate2():
	two_label.config(text = "Updated 2")


def ButtonUpdate3():
    three_label.config(text = "Updated 3")

def RandomButton():
	r = random.randint(1, 3)
	if r == 1:
		one_button.config(text = 'Randomly Picked')
	if r == 2:
		two_button.config(text = 'Randomly Picked')
	if r == 3:
		three_button.config(text = 'Randomly Picked')

#Create button
one_button = Button(root, text='Update 1', command=ButtonUpdate1)
two_button = Button(root, text='Update 2', command=ButtonUpdate2)
three_button = Button(root, text='Update 3', command=ButtonUpdate3)
random_button = Button(root, text='Random Pick', command=RandomButton)
one_label = Label(root, text='Label 1')
two_label = Label(root, text='Label 2')
three_label = Label(root, text='Label 3')

#pack
one_button.pack()
two_button.pack()
three_button.pack()
one_label.pack()
two_label.pack()
three_label.pack()
random_button.pack()

root.mainloop()
