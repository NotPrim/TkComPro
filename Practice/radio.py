from tkinter import *
import tkinter.messagebox
root = Tk()
root.title("Radio")
root.geometry("500x500")
language = IntVar()
language.set(2)


def showChoice():
    choice = language.get()
    if choice == 1:
        tkinter.messagebox.showinfo("แจ้งเตือน", "Python")
    elif choice == 2:
        tkinter.messagebox.showinfo("แจ้งเตือน", "Java")
    elif choice == 3:
        tkinter.messagebox.showinfo("แจ้งเตือน", "PHP")
    elif choice == 4:
        tkinter.messagebox.showinfo("แจ้งเตือน", "C#")


# เพิ่มตัวเลือกในโปรแกรม
Radiobutton(text="Python", variable=language, value=1, command=showChoice).grid(row=0, column=0)
Radiobutton(text="Java", variable=language, value=2, command=showChoice).grid(row=0, column=1)
Radiobutton(text="PHP", variable=language, value=3, command=showChoice).grid(row=0, column=2)
Radiobutton(text="C#", variable=language, value=4, command=showChoice).grid(row=0, column=3)

root.mainloop()