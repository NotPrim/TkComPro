from tkinter import *
from pages.System.Items import *


class DataLine:
    editable = False
    def __init__(this, master: Misc, name: str, price: str, row: int):
        this.nameEntry = Entry(master)
        this.nameEntry.insert(0, name)
        this.nameEntry.config(state='readonly')
        this.priceEntry = Entry(master)
        this.priceEntry.insert(0, price)
        this.priceEntry.config(state='readonly')
        this.editButton = Button(master, text="แก้ไข", command=this.editToggle)
        this.removetButton = Button(master, text="นำออก", command=this.selfDestroy)
        this.setRow(row)
    
    def setRow(this, line: int):
        this.nameEntry.grid(row=line, column=0)
        this.priceEntry.grid(row=line, column=1)
        this.editButton.grid(row=line, column=2)
        this.removetButton.grid(row=line, column=3)

    def editToggle(this):
        this.editable = not this.editable
        if this.editable:
            this.nameEntry.config(state=NORMAL)
            this.priceEntry.config(state=NORMAL)
        else:
            this.nameEntry.config(state='readonly')
            this.priceEntry.config(state='readonly')

    def selfDestroy(this):
        this.nameEntry.destroy()
        this.priceEntry.destroy()
        this.editButton.destroy()
        this.removetButton.destroy()


class DataEditor:
    def __init__(this) -> None:
        this.items = loadItemList()
        this.editor = Tk()
        this.editor.title("Editor")
        for i, k in enumerate(this.items, 0):
            DataLine(this.editor, k, this.items[k], i)
        # ทำปุ่ม Add ต่อท้าย
        # ปุ่ม Save?
        this.editor.mainloop()


if __name__ == "__main__":
    DataEditor()