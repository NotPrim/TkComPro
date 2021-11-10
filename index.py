from tkinter.font import BOLD
from pages.UI.LoginPage import *
from pages.System.Items import *
root = Tk()
root.title("python GUI")
root.geometry("1000x600+500+200")
root.resizable(0,0)

# หาสินค้า
def searchItem(*args):
    print(txt.get())
def leave(*args):
    root.focus()
    
# ช่องหาสินค้า
txt = StringVar()
txt.trace_add("write", searchItem)  # เรียกฟังก์ชันทุกครั้งที่เราพิมพ์
search = Entry(root, width=43, textvariable=txt)
search.pack(padx=5,pady=10,anchor=E)
search.bind("<Leave>",leave)

# goSearch = Button(left, text="Go!", bg="#7ADC6F", activebackground="#61b058", padx=10)
# goSearch.grid(row=0, column=2)

# ตัวแบ่งหน้าจอ
pane = PanedWindow(root)
pane.pack(fill=BOTH, expand=1)

# เพื่มพื้นที่ฝั่งซ้าย
left = ttk.Frame(pane)
left['borderwidth'] = 10
left['relief'] = 'solid'
pane.add(left)

# เพื่มพื้นที่ฝั่งขวา
right = ttk.Frame(pane, width=300)
right['borderwidth'] = 10
right['relief'] = 'solid'
pane.add(right)


# เปลี่ยนเมนูตามสถานะการ login
def loginToggle(*args):
    if adminLoggedin.get():
        myMenu.delete(1)
        # ปุ่ม logout เมื่อกดจะให้ยืนยันอีกที
        myMenu.add_cascade(label="Logout",
                           command=lambda: adminLoggedin.set(False) if messagebox.askyesno("Logout?", "Are you sure?") else None)
        myMenu.add_cascade(label="Add")
        myMenu.add_cascade(label="Edit")
        myMenu.add_cascade(label="Remove")
    else:
        myMenu.delete(1, 4)
        myMenu.add_cascade(
            label="Login", command=lambda: LoginWindow(adminLoggedin))


# ตัวแปรในระบบ
adminLoggedin = BooleanVar(root, False)
adminLoggedin.trace_add("write", loginToggle)

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)
# เพิ่มเมนูหลัก
myMenu.add_cascade(label="Login", command=lambda: LoginWindow(adminLoggedin))


productLabel = Label(left,text="Product",bg="red",width=100,foreground="white")
productLabel.grid(row=0,column=0)

productLabel = Label(right,text="Order",bg="green",width=35,foreground="white")
productLabel.grid(row=0,column=0)


root.mainloop()
