from tkinter import *


class OrderFrame(Frame):
    def __init__(self, root=None, parent=None, data=None, bouquet_id=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.flower_shop = data
        self.credit_card = StringVar()
        self.address = StringVar()
        self.delivery = StringVar()
        self.bouquet_id = bouquet_id
        self.init_order_frame()

    def init_order_frame(self):
        self.root.title("Order")
        self.root.configure(bd=10)
        self.root.columnconfigure((0, 1, 2), weight=1)
        self.root.rowconfigure((0, 2), weight=1)
        self.root.rowconfigure(1, weight=2)
        Label(self.root, text="Credit Card").grid(row=0, column=0)
        Entry(self.root, textvariable=self.credit_card, width=40).grid(row=0, column=1, columnspan=2)
        Label(self.root, text="Address").grid(row=1, column=0, pady=5)
        Entry(self.root, textvariable=self.address, width=40).grid(row=1, column=1, columnspan=2)
        Label(self.root, text="Delivery Time and Date").grid(row=2, column=0)
        Entry(self.root, textvariable=self.delivery, width=40).grid(row=2, column=1, columnspan=2)
        Button(self.root, text="Buy", bg="LightSteelBlue2", width="6", height="1",
               command=lambda: self.parent.on_confirmed_buy(self.bouquet_id, self.address,
                                                            self.credit_card)).grid(row=4, column=1)
        Button(self.root, text="Cancel", bg="LightSteelBlue2", width="6", height="1",
               command=lambda: self.on_closing()).grid(row=4, column=2)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def on_closing(self):
        self.parent.on_cancelled_buy()

