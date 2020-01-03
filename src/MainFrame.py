from tkinter import *
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame
from InfoFrame import InfoFrame


class MainFrame(Frame):
    def __init__(self, root=None, data=None, ncols=None, nrows=None):
        Frame.__init__(self, root)
        self.root = root
        self.ncols = ncols
        if ncols is None:
            self.ncols = 4
        self.nrows = nrows
        if nrows is None:
            self.nrows = 3
        self.frames = []
        self.flower_shop = data
        self.init_main_frame()
        self.login_dialog = None
        self.register_dialog = None
        self.info_dialog = None

    def init_main_frame(self):
        self.root.title(self.flower_shop.name)
        self.display_menu()
        self.root.columnconfigure(tuple(range(0, self.ncols)), weight=1)
        self.root.rowconfigure(tuple(range(0, self.nrows)), weight=1)
        for row in range(0, self.nrows):
            for col in range(0, self.ncols):
                frame = Frame(self.root)
                frame.grid(row=row, column=col, padx=5, pady=5)
                self.frames.append(frame)
        Label(self.frames[0], text="I am").pack()
        Label(self.frames[0], text='the first grid position').pack()
        Label(self.frames[1], text="I am").pack()
        Label(self.frames[1], text='at position (0, 1)').pack()
        Label(self.frames[6], text="I am").pack()
        Label(self.frames[6], text='at position (1, 1)').pack()
        Label(self.frames[7], text="I am").pack()
        Label(self.frames[7], text='at position (1, 2)').pack()
        Label(self.frames[len(self.frames) - 1], text="I am").pack()
        Label(self.frames[len(self.frames) - 1], text='the last grid position').pack()

    def display_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        info = Menu(menu)
        menu.add_cascade(label="Home")
        menu.add_cascade(label="Flowers")
        menu.add_cascade(label="Bouquets")
        info.add_command(label="Contact Us", command=self.information)
        menu.add_cascade(label="Info", menu=info)
        user = Menu(menu)
        if self.flower_shop.logged_user is None:
            menu.add_cascade(label="User", menu=user)
            user.add_command(label="Login", command=self.login)
            user.add_command(label="Register", command=self.register)
        else:
            menu.add_cascade(label=self.flower_shop.logged_user.username, menu=user)
            user.add_command(label="Log out", command=self.logout)

    def login(self):
        self.login_dialog = Toplevel()
        self.login_dialog.geometry("400x300")
        self.login_dialog.focus_force()
        self.login_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        LoginFrame(root=self.login_dialog, parent=self, data=self.flower_shop)

    def register(self):
        self.register_dialog = Toplevel()
        self.register_dialog.geometry("400x300")
        self.register_dialog.focus_force()
        self.register_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        RegisterFrame(root=self.register_dialog, parent=self, data=self.flower_shop)

    def on_successful_login(self):
        print(self.flower_shop.to_json())
        self.login_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()
        self.display_menu()

    def on_successful_register(self):
        print(self.flower_shop.to_json())
        self.flower_shop.save('../flower_shop.json')
        self.register_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()
        self.display_menu()

    def information(self):
        self.info_dialog = Toplevel()
        self.info_dialog.geometry("200x90")
        self.info_dialog.focus_force()
        self.info_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        InfoFrame(root=self.info_dialog, parent=self)

    def logout(self):
        self.flower_shop.logged_user = None
        self.display_menu()
