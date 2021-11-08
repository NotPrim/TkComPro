from tkinter import *
root = Tk()
root.title("Data Entry")
root.geometry("500x500")

Label(text="name").grid(row=0)
Label(text="surname").grid(row=1)
Label(text="tel.").grid(row=2)

et1 = Entry()
et1.grid(row=0, column=1)
et1.insert(0, "Sanfong")
et2 = Entry()
et2.grid(row=1, column=1)
et3 = Entry()
et3.grid(row=2, column=1)


def clearText():
    et1.delete(0, END)
    et2.delete(0, END)
    et3.delete(0, END)


clearButton = Button(text="clear", command=clearText).grid(row=3, column=1)

root.mainloop()