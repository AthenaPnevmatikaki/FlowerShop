from tkinter import *


class LoginFrame(Frame):
    def __init__(self, root=None, parent=None, data=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.flower_shop = data
        self.init_login_frame()

    def init_login_frame(self):
        global username_verify, password_verify, username_entry1, password_entry1
        self.root.title("Login")
        username_verify = StringVar()
        password_verify = StringVar()
        Label(self.root, text="Username").pack()
        username_entry1 = Entry(self.root, textvariable=username_verify)
        username_entry1.pack()
        Label(self.root, text="password").pack()
        password_entry1 = Entry(self.root, textvariable=password_verify)
        password_entry1.pack()
        Label(self.root, text="").pack()
        Button(self.root, text="Login", bg="LightSteelBlue2", width="12", height="1", command=lambda: self.login_verify()).pack()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def login_verify(self):
        username_found = False
        for user in self.flower_shop.users:
            if user.username == str(username_verify.get()):
                username_found = True
                if user.password == str(password_verify.get()):
                    self.flower_shop.logged_user = user
                    self.parent.on_successful_login()
                else:
                    Label(self.root, text="Wrong username or password.", fg="red", font=("callibri", 13)).pack()
        if not username_found:
            Label(self.root, text="Wrong username or password.", fg="red", font=("callibri", 13)).pack()

    def on_closing(self):
        self.parent.on_successful_login()