from tkinter import *
root = Tk()
root.title("GUI Program")
root.geometry("500x500")



# แสดงข้อความ
myLabel = Label(root, text="Hello World", fg="red", font=20).pack()
# กล่องข้อความ
txt = StringVar()
textBox = Entry(root, textvariable=txt).pack()


def showMessage():
    msg = txt.get() if txt.get() != "" else "Click!"
    Label(root, text=msg).pack()


def openWindow():
    # หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("ผลการทำงาน")
    myWindow.geometry("300x300")

# ปุ่ม
b1 = Button(root, text="Click", fg="white", bg="green", command=showMessage).pack()
b2 = Button(root, text="Report", fg="black", bg="yellow", command=openWindow).pack()
'''
.pack() ตรงกลาง
.place(x=0, y=0) เลือกตำแหน่ง
.grid(row=0, column=0) เลีอกตำแหน่งตาราง
'''


root.mainloop()