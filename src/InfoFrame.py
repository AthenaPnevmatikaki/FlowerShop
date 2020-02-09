from tkinter import *


class InfoFrame(Frame):
    def __init__(self, root=None, parent=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.init_info_frame()

    def init_info_frame(self):
        self.root.title = "About Us"
        self.root.geometry("300x100")
        self.root.configure(bg="RosyBrown2")
        Label(self.root, text="Telephone: **********",bg="RosyBrown2").pack()
        Label(self.root, text="Address: ************",bg="RosyBrown2").pack()
        Label(self.root, text="Email: *******@flowershop.com",bg="RosyBrown2").pack()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def on_closing(self):
        self.parent.root.attributes('-disabled', 'false')
        self.parent.root.focus_force()
        self.root.destroy()
