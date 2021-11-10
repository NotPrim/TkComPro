from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# สร้างหน้าต่าง login
def LoginWindow(adminLoggedin: BooleanVar):
    # โหลดข้อมูลของ admin
    adminFile = open("assets/user/admin.txt", "r")
    adminUser, adminPass = adminFile.read().split(',')
    adminFile.close()

    # เช็คการ login และปิดหน้าต่าง
    def closeWindow():
        if userEntry.get() == adminUser and passEntry.get() == adminPass:  # login ผ่าน
            if adminLoggedin != None:
                adminLoggedin.set(True)
        else:
            messagebox.showerror("เข้าสู่ระบบไม่สำเร็จ", "ชื่อผู้ใช้ หรือ รหัสผ่านไม่ถูกต้อง")
        window.destroy()

    # สร้างหน้าต่างเข้าสู่ระบบ
    window = Tk()
    window.resizable(0, 0)
    window.title("เข้าสู่ระบบ")
    Label(window, text="ชื่อผู้ใช้").grid(row=0, column=0, padx=5)
    Label(window, text="รหัสผ่าน").grid(row=1, column=0)
    userEntry = Entry(window)
    passEntry = Entry(window, show='*')
    userEntry.grid(row=0, column=1)
    passEntry.grid(row=1, column=1, padx=5)
    loginButton = Button(window, text="เข้าสู่ระบบ!", bg="#7ADC6F", activebackground="#61b058", padx=10, command=closeWindow)
    loginButton.grid(row=2, column=0, columnspan=2, pady=5)
    window.mainloop()


if __name__ == "__main__":
    LoginWindow(None)