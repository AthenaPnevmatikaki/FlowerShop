from tkinter import *
from User import User


class RegisterFrame(Frame):
    def __init__(self, root=None, parent=None, data=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.flower_shop = data
        self.init_register_frame()

    def init_register_frame(self):
        global username, password, emailaddress, username_entry, password_entry, emailaddress_entry
        self.root.title("Register")
        username = StringVar()
        password = StringVar()
        emailaddress = StringVar()
        Label(self.root, text="Username").pack()
        username_entry = Entry(self.root, textvariable=username)
        username_entry.pack()
        Label(self.root, text="password").pack()
        password_entry = Entry(self.root, textvariable=password)
        password_entry.pack()
        Label(self.root, text="Email address").pack()
        emailaddress_entry = Entry(self.root, textvariable=emailaddress)
        emailaddress_entry.pack()
        Label(self.root, text="").pack()
        Button(self.root, text="Register", bg="red", width="12", height="1", command=lambda:self.register_user()).pack()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

    def register_user(self):
        user = User(user_dict={'email': str(emailaddress.get()), 'password': str(password.get()),
                               'username': str(username.get())})
        if self.flower_shop.add_user(user):
            self.flower_shop.logged_user = self.flower_shop.users[self.flower_shop.users_id_counter - 1]
            self.parent.on_successful_register()
        else:
            username_entry.delete(0, 'end')
            Label(self.root, text="Username already exists", fg="red", font=("callibri", 13)).pack()

    def on_closing(self):
        self.parent.on_successful_register()

