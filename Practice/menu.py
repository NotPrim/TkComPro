from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Menu GUI")
root.geometry("500x500")

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)


def newWindow():
    window = Tk()
    window.title("new Window")
    window.mainloop()


def aboutProgram():
    tkinter.messagebox.showinfo("รายละเอียด", "ผมเอง")


def exitProgram():
    confirm = tkinter.messagebox.askyesno("ยืนยัน", "ปิดโปรแกรมไหม?")
    if confirm:
        root.destroy()


# เมนูย่อย
menuItem = Menu()
menuItem.add_command(label="New Window", command=newWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About", command=aboutProgram)
menuItem.add_command(label="Exit", command=exitProgram)

# เพิ่มเมนูหลัก
myMenu.add_cascade(label="File", menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()