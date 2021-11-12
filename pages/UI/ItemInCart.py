from tkinter import *

cartItemList = []


class CartItem:
    def __init__(self, master: Misc, name: str, price: str, count: int):
        self.nameLabel = Label(master, text=name)
        self.nameLabel.grid(row=count, column=0, sticky=W)
        self.priceLabel = Label(master, text=price)
        self.priceLabel.grid(row=count, column=1, sticky=E)
        self.deleteButton = Button(master, text="นำออก", bg="#d33",
                                   fg="#fff", activebackground="#d11", activeforeground="#fff", command=lambda: deleteCartItem(self))
        self.deleteButton.grid(row=count, column=2, sticky=E, pady=3)

    def changeRow(self, count: int):
        self.nameLabel.grid(row=count, column=0, sticky=W)
        self.priceLabel.grid(row=count, column=1, sticky=E)
        self.deleteButton.grid(row=count, column=2, sticky=E, pady=3)


def addCartItem(master: Misc, name: str, price: str):
    cartItemList.append(CartItem(master, name, price, len(cartItemList) + 1))


def cartArrange():
    for row, item in enumerate(cartItemList, 1):
        item.changeRow(row)


def deleteCartItem(cartItem: CartItem):
    cartItem.nameLabel.destroy()
    cartItem.priceLabel.destroy()
    cartItem.deleteButton.destroy()
    cartItemList.remove(cartItem)
    cartArrange()
