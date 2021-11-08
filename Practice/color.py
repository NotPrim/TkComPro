from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk()
root.title("GUI Color")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    Label(root, text="Hello", bg=color[1]).pack()


def selectFile():
    fileopen = askopenfilename()
    fileContent = open(fileopen, encoding="utf8")
    Label(text=fileContent.read()).pack()


btn1 = Button(root, text="select color", font=20, command=selectColor).pack()
btn2 = Button(root, text="select file", font=20, command=selectFile).pack()
root.mainloop()