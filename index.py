from tkinter.font import BOLD
from types import CellType
from pages.UI.LoginPage import *
from pages.System.Items import *
from pages.UI.ItemInCart import *
from pages.UI.EditPage import *
root = Tk()
root.title("python GUI")
root.geometry("800x600+500+200")
root.resizable(0, 0)
# ปุ่ม clear
# หาสินค้า
def searchItem(*args):
    itemDict = searchSort(txt.get()) # เรียงลำดับรายการใหม่
    for i in table.get_children(): # ลบรายการทั้งหมดออก
        table.delete(i)
    for i, key in enumerate(itemDict, 1): # ใส่กลับเข้าไปใหม่
        table.insert(parent='', index='end', iid=i, text='',values=(i, key, itemDict[key]))


# ช่องหาสินค้า
navbar = Frame(root)
navbar.pack(fill="x")

txt = StringVar()
txt.trace_add("write", searchItem)  # เรียกฟังก์ชันทุกครั้งที่เราพิมพ์
search = Entry(navbar, width=44, textvariable=txt)
search.pack(padx=5, pady=10,side=LEFT)
search.bind("<Leave>", lambda *a: root.focus()) # เปลี่ยนมาใช้ lambda

buyButton = Button(navbar,text="สั่งซื้อ",bg="#0D6EFD",fg="#fff",activebackground="#1C76FD",activeforeground="#fff")
buyButton.pack(padx=5, pady=10,side=RIGHT)


# ตัวแบ่งหน้าจอ
pane = PanedWindow(root)
pane.pack(fill=BOTH, expand=1)

# เพื่มพื้นที่ฝั่งซ้าย
left = ttk.Frame(pane, width=200)
left['borderwidth'] = 0
left['relief'] = 'solid'
pane.add(left)
pane.paneconfig(left, minsize=520) # ตั้งค่าความกว้างขั้นต่ำ

# เพื่มพื้นที่ฝั่งขวา
right = ttk.Frame(pane)
right['borderwidth'] = 1
right['relief'] = 'solid'
pane.add(right)
pane.paneconfig(right, minsize=300) # ตั้งค่าความกว้างขั้นต่ำ


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
        myMenu.add_cascade(label="เข้าสู่ระบบ", command=lambda: LoginWindow(adminLoggedin))


# ตัวแปรในระบบ
adminLoggedin = BooleanVar(root, False)
adminLoggedin.trace_add("write", loginToggle)

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

# เพิ่มเมนูหลัก
myMenu.add_cascade(label="เข้าสู่ระบบ", command=lambda: LoginWindow(adminLoggedin))

# สร้างตารางสำหรับกดสั่งสินค้า
productLabel = Label(left, text="รายการสินค้า", bg="#062f3c", width=74, foreground="white")
productLabel.grid(row=0, column=0)

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


# เลือกสินค้า
def OnDoubleClick(event):
    items = table.identify('item', event.x, event.y)
    itemData = table.item(items, "values")
    if len(itemData):
        addCartItem(right, itemData[1], itemData[2])
    print("Key : ", itemData)


# เอารายการใส่ลงตาราง
for i, key in enumerate(itemDict, 1):
    table.insert(parent='', index='end', iid=i, text='', values=(i, key, itemDict[key]))

table.bind("<Double-1>", OnDoubleClick) # เมื่อดับเบิลคลิกที่สินค้าจะเรียก OnDoubleClick
table.grid()

# รถเข็น แสดงสินค้าที่สั่ง
productLabel = Label(right, text="ยอดการสั่งซื้อ", bg="#059669",width=38, foreground="white")
productLabel.grid(row=0, column=0, columnspan=3)

# cart = ttk.Treeview(right)
# cart['columns'] = ('ID', 'Name', 'Price')
# cart.column("#0", width=0, stretch=NO)
# cart.column("ID", anchor=W, width=30)
# cart.column("Name", anchor=W, width=100)
# cart.column("Price", anchor=W, width=30)

# cart.heading("#0", text="", anchor=W)
# cart.heading("ID", text="ลำดับ", anchor=W)
# cart.heading("Name", text="ชื่อเมนู", anchor=W)
# cart.heading("Price", text="ราคา (บาท)", anchor=W)
# cart.grid(row=1)

root.mainloop()
