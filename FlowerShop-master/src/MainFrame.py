from tkinter import *
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame
from InfoFrame import InfoFrame


class MainFrame(Frame):
    def __init__(self, root=None, data=None):
        Frame.__init__(self, root)
        self.root = root
        self.flower_shop = data
        self.init_main_frame()
        self.login_dialog = None
        self.register_dialog = None
        self.info_dialog=None

    def init_main_frame(self):
        self.root.title(self.flower_shop.name)
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.root)
        self.root.config(menu=menu)
        user = Menu(menu)
        menu.add_cascade(label="Home")
        menu.add_cascade(label="Flowers")
        menu.add_cascade(label="Bouquets")
        info=Menu(menu)
        info.add_command(label="Contact Us",command=self.infor)
        menu.add_cascade(label="Info",menu=info)
        user.add_command(label="Login", command=self.login)
        user.add_command(label="Register", command=self.register)
        menu.add_cascade(label="User", menu=user,)
    def login(self):
        self.login_dialog = Toplevel()
        self.login_dialog.geometry("400x300")
        self.login_dialog.focus_force()
        LoginFrame(root=self.login_dialog, parent=self, data=self.flower_shop)

    def register(self):
        self.register_dialog = Toplevel()
        self.register_dialog.geometry("400x300")
        self.register_dialog.focus_force()
        RegisterFrame(root=self.register_dialog, parent=self, data=self.flower_shop)

    def on_successful_login(self):
        print(self.flower_shop.to_json())
        self.login_dialog.destroy()
        # TODO: show logged in user in GUI

    def on_successful_register(self):
        print(self.flower_shop.to_json())
        self.flower_shop.save('../athena_flowers.json')
        self.register_dialog.destroy()
        # TODO: show logged in user in GUI

    def infor(self):
        self.info_dialog=Toplevel()
        self.info_dialog.geometry("200x90")
        self.info_dialog.focus_force()
        InfoFrame(root=self.info_dialog,parent=self)