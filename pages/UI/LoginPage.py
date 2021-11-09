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
            messagebox.showerror("Login Failed", "username or password is invalid")
        window.destroy()

    window = Tk()
    window.title("Login")
    Label(window, text="username").grid(row=0, column=0, padx=5)
    Label(window, text="password").grid(row=1, column=0)
    userEntry = Entry(window)
    passEntry = Entry(window, show='*')
    userEntry.grid(row=0, column=1)
    passEntry.grid(row=1, column=1, padx=5)
    loginButton = Button(window, text="Login!", bg="#7ADC6F", activebackground="#61b058", padx=10, command=closeWindow)
    loginButton.grid(row=2, column=0, columnspan=2, pady=5)
    window.mainloop()


if __name__ == "__main__":
    LoginWindow(None)