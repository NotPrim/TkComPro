from tkinter import *
try:
    from Items import *
except ModuleNotFoundError:
    from views.Items import *


class DataLine:
    editable = False

    def __init__(this, master: Misc, name: str, price: str, row: int, selfContainer: list = list()):
        this.nameEntry = Entry(master, width=40)
        this.nameEntry.insert(0, name)
        this.nameEntry.config(state='readonly')
        this.priceEntry = Entry(master, width=10)
        this.priceEntry.insert(0, price)
        this.priceEntry.config(state='readonly')
        this.editButton = Button(master, text="แก้ไข", width=5,
                                 command=this.editToggle, bg="#FFC107", activebackground="#FBBC00")
        this.removetButton = Button(master, text="นำออก", width=5, command=this.selfDestroy,
                                    bg="#d33", fg="#fff", activebackground="#d11", activeforeground="#fff")
        this.setRow(row)
        this.selfContainer = selfContainer

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
        if len(this.selfContainer) > 1:
            this.nameEntry.destroy()
            this.priceEntry.destroy()
            this.editButton.destroy()
            this.removetButton.destroy()
            if this.selfContainer.count(this):
                this.selfContainer.remove(this)
        else:
            this.nameEntry.config(state=NORMAL)
            this.priceEntry.config(state=NORMAL)
            this.nameEntry.delete(0, END)
            this.priceEntry.delete(0, END)
            this.editToggle()
            this.editToggle()

    def extract(this):
        return this.nameEntry.get(), this.priceEntry.get()


class DataEditor:
    lineList = []

    def __init__(this) -> None:
        this.items = loadItemList()
        this.editor = Tk()
        this.editor.title("Editor")
        Label(this.editor, text="ชื่อสินค้า").grid(row=0, column=0)
        Label(this.editor, text="ราคา").grid(row=0, column=1)
        for i, k in enumerate(this.items, 1):
            this.lineList.append(
                DataLine(this.editor, k, this.items[k], i, this.lineList))
        this.createAdd()
        # ปุ่ม Save?
        this.editor.mainloop()

    def AddItem(this):
        this.addButton.destroy()
        this.saveButton.destroy()
        this.lineList.append(
            DataLine(this.editor, "", "0", len(this.lineList) + 1, this.lineList))
        for i, dl in enumerate(this.lineList, 1):
            dl.setRow(i)
        this.createAdd()

    def createAdd(this):
        this.addButton = Button(this.editor, text="เพิ่มรายการสินค้า", command=this.AddItem,
                                bg="#198754", fg="#fff", activebackground="#157547", activeforeground="#fff")
        this.addButton.grid(row=len(this.lineList) + 1,
                            columnspan=2, sticky="nsew")
        this.saveButton = Button(this.editor, text="บันทึก", command=this.saveToFile,
                                 bg="#0D6EFD", fg="#fff", activebackground="#1C76FD", activeforeground="#fff")
        this.saveButton.grid(row=len(this.lineList) + 1,
                             column=2, columnspan=2, sticky="nsew")

    def saveToFile(this, fileName: str = "assets/products/ItemList.csv"):
        file = open(fileName, "w")
        file.writelines((",".join(data.extract()) +
                        "\n" for data in this.lineList if data.extract()[0] != ""))
        file.close()


if __name__ == "__main__":
    DataEditor()
