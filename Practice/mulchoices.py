from tkinter import *

root = Tk()
root.title("Multiple Choices")
root.geometry("500x500")


def showChoice():
    txt = "you choose " + "Python " * l1.get() + "Java " * l2.get() + "PHP " * l3.get() + "C#" * l4.get()
    Label(text=txt).pack(anchor=W)


l1 = BooleanVar()
Checkbutton(text="Python", variable=l1).pack(anchor=W)
l2 = BooleanVar()
Checkbutton(text="Java", variable=l2).pack(anchor=W)
l3 = BooleanVar()
Checkbutton(text="PHP", variable=l3).pack(anchor=W)
l4 = BooleanVar()
Checkbutton(text="C#", variable=l4).pack(anchor=W)

Button(text="show", command=showChoice).pack(anchor=W)
root.mainloop()