from tkinter import *


class InfoFrame(Frame):
    def __init__(self, root=None, parent=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.init_info_frame()

    def init_info_frame(self):
        self.root.title=("Info")
        Label(self.root, text="Telephone: **********").pack()
        Label(self.root, text="Address: ************").pack()
        Label(self.root, text="Email: *******@flowershop.com").pack()