from tkinter.font import BOLD
from types import CellType
from pages.UI.LoginPage import *
from pages.System.Items import *
root = Tk()
root.title("python GUI")
root.geometry("800x600+500+200")
root.resizable(0, 0)

# หาสินค้า


def searchItem(*args):
    itemDict = searchSort(txt.get())
    for i in table.get_children():
        table.delete(i)
    for i, key in enumerate(itemDict, 1):
        table.insert(parent='', index='end', iid=i, text='',values=(i, key, itemDict[key]))


def leave(*args):
    root.focus()


# ช่องหาสินค้า

txt = StringVar()
txt.trace_add("write", searchItem)  # เรียกฟังก์ชันทุกครั้งที่เราพิมพ์
search = Entry(root, width=44, textvariable=txt)
search.pack(padx=5, pady=10, anchor=E)
search.bind("<Leave>", leave)
# goSearch = Button(left, text="Go!", bg="#7ADC6F", activebackground="#61b058", padx=10)
# goSearch.grid(row=0, column=2)

# ตัวแบ่งหน้าจอ
pane = PanedWindow(root)
pane.pack(fill=BOTH, expand=1)

# เพื่มพื้นที่ฝั่งซ้าย
left = ttk.Frame(pane, width=200)
left['borderwidth'] = 0
left['relief'] = 'solid'
pane.add(left)

# เพื่มพื้นที่ฝั่งขวา
right = ttk.Frame(pane)
right['borderwidth'] = 0
right['relief'] = 'solid'
pane.add(right)


# เปลี่ยนเมนูตามสถานะการ login
def loginToggle(*args):
    if adminLoggedin.get():
        myMenu.delete(1)
        # ปุ่ม logout เมื่อกดจะให้ยืนยันอีกที
        
        myMenu.add_cascade(label="เพิ่มข้อมูล")
        myMenu.add_cascade(label="แก้ไขข้อมูล")
        myMenu.add_cascade(label="ลบข้อมูล")
        myMenu.add_cascade(label="ออกจากระบบ",
                           command=lambda: adminLoggedin.set(False) if messagebox.askyesno("ออกจากระบบ?", "คุณแน่ใจใช่ไหมที่จะออกจากระบบ?") else None)
    else:
        myMenu.delete(1, 4)
        myMenu.add_cascade(
            label="เข้าสู่ระบบ", command=lambda: LoginWindow(adminLoggedin))


# ตัวแปรในระบบ
adminLoggedin = BooleanVar(root, False)
adminLoggedin.trace_add("write", loginToggle)

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)
# เพิ่มเมนูหลัก
myMenu.add_cascade(label="เข้าสู่ระบบ", command=lambda: LoginWindow(adminLoggedin))


productLabel = Label(left, text="รายการสินค้า", bg="red",
                     width=74, foreground="white")
productLabel.grid(row=0, column=0)


# Table
table = ttk.Treeview(left, height=300)
table['columns'] = ('ID', 'Name', 'Price')

table.column("#0", width=0, stretch=NO)
table.column("ID", anchor=W, width=80)
table.column("Name", anchor=W, width=360)
table.column("Price", anchor=W, width=80)

table.heading("#0", text="", anchor=W)
table.heading("ID", text="ลำดับ", anchor=W)
table.heading("Name", text="ชื่อเมนู", anchor=W)
table.heading("Price", text="ราคา (บาท)", anchor=W)


def OnDoubleClick(event):
    items = table.identify('item', event.x, event.y)
    print("Key : ", table.item(items, "values"))


for i, key in enumerate(itemDict, 1):
    table.insert(parent='', index='end', iid=i, text='',
                 values=(i, key, itemDict[key]))
table.bind("<Double-1>", OnDoubleClick)
table.grid()


productLabel = Label(right, text="ยอดการสั่งซื้อ", bg="green",
                     width=38, foreground="white")
productLabel.grid(row=0, column=0)

root.mainloop()
