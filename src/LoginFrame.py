from tkinter import *


class LoginFrame(Frame):
    def __init__(self, root=None, parent=None, data=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.flower_shop = data
        self.init_login_frame()

    def init_login_frame(self):
        self.root.title("Login")
        ok_btn = Button(self.root, text="OK", command=self.login)
        ok_btn.pack()

    def login(self):
        print("Logged in")
        self.flower_shop.user = "apne"
        self.root.destroy()
        self.parent.on_successful_login()
