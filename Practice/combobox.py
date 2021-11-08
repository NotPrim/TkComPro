from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combo Box")

Label(text="Address", font=20).grid(row=0, column=0)
choice = StringVar(value="Province")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("กรุงเทพ", "เชียงใหม่", "กระบี่", "ภูเก็ต", "ชลบุรี")
combo.grid(row=0, column=1)


def selectCity():
    Label(text=choice.get()).grid(row=2, column=1)


btn = Button(text="ส่งข้อมูล", command=selectCity).grid(row=1, column=1)
root.mainloop()