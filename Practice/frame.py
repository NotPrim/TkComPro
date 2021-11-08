from tkinter import *
from tkinter import ttk
root = Tk()
l = ttk.Label(root, text="Starting...")
l.grid(row=0, column=0)
f = ttk.Frame(root)
f['padding'] = (5,7,10,12) # left: 5, top: 7, right: 10, bottom: 12
f['borderwidth'] = 10
f['relief'] = 'solid'
f.grid(row=0, column=1)
l = ttk.Label(f, text="2...")
l.pack()
root.mainloop()
