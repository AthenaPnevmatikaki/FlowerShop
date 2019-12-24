from tkinter import *

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

    def register_user(self):
        username_info = username.get()
        password_info = password.get()
        emailaddress_info = emailaddress.get()

        #user = User(user_dict={'id':'1','email': str(emailaddress_info), 'password':str(password_info)})
        #user.to_json()

        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info + "\n")
        file.write(emailaddress_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        emailaddress_entry.delete(0, END)
        Label(self.root, text="Επιτυχής Εγγραφή", fg="green", font=("callibri", 13)).pack()

